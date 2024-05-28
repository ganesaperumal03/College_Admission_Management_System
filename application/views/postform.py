from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonal, Admissionaddress,image_form, Admissionsslc, AdmissionMark, academic_Details,AdmissionDiploma,certificateform,transportform
from application.models import Personal_Details,Diplomo, HSC_Marks, Academic_Details,Diplomo,certificates
from datetime import datetime
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator
from django.conf import settings
import pandas as pd
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

# def generate_unique_admission_number():
#     current_year_last_two_digits = datetime.now().strftime("%y")
#     add_digit = int(current_year_last_two_digits) + 4
#     count = Personal_Details.objects.count() + 1
#     return f"{current_year_last_two_digits}{add_digit:02d}{count:03d}"


def generate_unique_admission_number():
    current_year = datetime.now().year
    add_digit = current_year + 1
    count = Personal_Details.objects.count() + 1
    return f"{current_year}-{add_digit % 100:02d}/{count:03d}"



def index(request,):
    return render(request, "index.html")

def post_index(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    if Aadhaar_Number is not None:
        if not Personal_Details.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            return render(request, "postform/personal.html",{'Aadhaar_Number':Aadhaar_Number})
    return render(request, "postform/index.html")


from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            email = User.objects.get(username=username).email
            request.session['userdata'] = email

            # Check user's email address and redirect accordingly
            if 'gmadmin@ritrjpm.ac.in' in email:
                return redirect('dashboard')
            elif 'ayyachamy@ritrjpm.ac.in' in email:
                return redirect('dashboard')
            elif 'prabhak@ritrjpm.ac.in' in email:
                return redirect('dashboard')
            elif 'muthumarik@ritrjpm.ac.in' in email:
                return redirect('dashboard')
            elif 'principal@ritrjpm.ac.in' in email:
                return redirect('dashboard')
            elif 'hodad@ritrjpm.ac.in' in email:
                return redirect('ad')
            elif 'hodcse@ritrjpm.ac.in' in email:
                return redirect('cse')
            elif 'hodcivil@ritrjpm.ac.in' in email:
                return redirect('civil')
            elif 'hodeee@ritrjpm.ac.in' in email:
                return redirect('eee')
            elif 'hodece@ritrjpm.ac.in' in email:
                return redirect('ece')
            elif 'hodmech@ritrjpm.ac.in' in email:
                return redirect('mech')
            elif 'hodit@ritrjpm.ac.in' in email:
                return redirect('it')
            elif 'hodcsbs@ritrjpm.ac.in' in email:
                return redirect('csbs')
            else:
                # Default redirect for users with unrecognized email
                return redirect('dashboard')

        else:
            error_message = "Invalid username or password. Please try again."

    return render(request, "sigin/login.html", {'error_message': error_message})


from application.form import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user
            auth_login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'sigin/sigin.html', {'form': form})




year = datetime.now().strftime("%Y")


def save_uploaded_images(file_dict, admission_number):
    # Use current year if 'year' is not provided
    year = datetime.now().year
    profile_images_directory = os.path.join(settings.MEDIA_ROOT, 'profile_images', str(year), str(admission_number))
    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        base_file_name = f'{admission_number}_{field_name}_{file_obj.name}'
        file_path = os.path.join(profile_images_directory, base_file_name)

        # Check if the file already exists, if yes, append a number
        counter = 1
        while os.path.exists(file_path):
            new_file_name = f'{admission_number}_{field_name}_{counter}_{file_obj.name}'
            file_path = os.path.join(profile_images_directory, new_file_name)
            counter += 1

        with open(file_path, 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        # Store relative path to media root
        file_paths[field_name] = os.path.relpath(file_path, settings.MEDIA_ROOT)

    return file_paths


def postform(request):
    if request.method == 'POST':
        form = AdmissionPersonal(request.POST, request.FILES)
        if form.is_valid():
            # Generate a unique admission number
            admission_number = generate_unique_admission_number()

            admission_number = str(admission_number)

            request.session['personal_data'] = {**form.cleaned_data}

            request.session['personal_data']['Date_of_Birth'] = form.cleaned_data['Date_of_Birth'].isoformat()
            admissionFor = form.cleaned_data['admissionFor']
            return redirect('address', admission_number=admission_number, admissionFor=admissionFor)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionPersonal()
    return render(request, "postform/personal.html", {'form': form})

def address(request, admission_number, admissionFor):
    excel_file_path = 'district.csv'
    # Read the Excel file
    try:
        df = pd.read_csv(excel_file_path)
    except pd.errors.EmptyDataError:
        # Handle the case where the Excel file is empty
        df = pd.DataFrame(columns=['District'])
    district = df['District'].tolist()


    excel_file_path1 = 'taluk.csv'
    try:
        df1 = pd.read_csv(excel_file_path1)
    except pd.errors.EmptyDataError:
        # Handle the case where the Excel file is empty
        df1 = pd.DataFrame(columns=['TALUK'])
    TALUK = df1['TALUK'].tolist()
    if request.method == 'POST':
        form = Admissionaddress(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['address_data'] = {**form.cleaned_data}
            return redirect('sslc', admission_number=admission_number, admissionFor=admissionFor)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = Admissionaddress()
    return render(request, "postform/address.html", {'form': form, 'admission_number': admission_number,'district':district,'TALUK':TALUK})


def sslc(request, admission_number, admissionFor):
    year = int(datetime.now().strftime("%Y"))
    year_of_passing=[year-6,year-5,year-4,year-3,year-2,year-1,year]
    excel_file_path = 'df.csv'
    # Read the Excel file
    try:
        df = pd.read_csv(excel_file_path)
    except pd.errors.EmptyDataError:
        # Handle the case where the Excel file is empty
        df = pd.DataFrame(columns=['School_Name'])

    # Extract school names
    school_names = df['School_Name'].tolist()
    if request.method == 'POST':
        form = Admissionsslc(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['sslc_data'] = {**form.cleaned_data}
            if admissionFor == 'I_Year':
                # Redirect to the 1st year address function
                return redirect('hsc', admission_number=admission_number)
            elif admissionFor == 'II_Year':
                # Redirect to the 2nd year sslc function
                return redirect('diploma', admission_number=admission_number)
            else:
                # Handle other cases or redirect to an error page
                return render(request, "postform/error.html", {'error_message': 'Invalid AdmissionFor value'})
        else:
            return render(request, "postform/error.html", {'form': form})
    else:

        form = Admissionsslc()
    return render(request, "postform/sslc.html", {'form': form, 'admission_number': admission_number,'school_names':school_names,"year_of_passing":year_of_passing})


def hsc(request, admission_number):
    year = int(datetime.now().strftime("%Y"))
    year_of_passing=[year-4,year-3,year-2,year-1,year]
    excel_file_path = 'df.csv'
    # Read the Excel file
    try:
        df = pd.read_csv(excel_file_path)
    except pd.errors.EmptyDataError:
        # Handle the case where the Excel file is empty
        df = pd.DataFrame(columns=['School_Name'])

    # Extract school names
    school_names = df['School_Name'].tolist()
    if request.method == 'POST':
        form = AdmissionMark(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['hsc_data'] = {**form.cleaned_data}
            return redirect('academic_details', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionMark()
    return render(request, "postform/hsc.html", {'form': form, 'admission_number': admission_number,'school_names':school_names,"year_of_passing":year_of_passing})

def diploma(request, admission_number):
    if request.method == 'POST':
        form = AdmissionDiploma(request.POST)
        if form.is_valid():
            request.session['diploma_data'] = {**form.cleaned_data}
            Diploma_apply_for = form.cleaned_data['Diploma_apply_for']
            if Diploma_apply_for == 'Diploma_Iyear':
                # Redirect to the 1st year address function
                return redirect('academic_details', admission_number=admission_number)
            elif Diploma_apply_for == 'Diploma_IIyear':
                # Redirect to the 2nd year sslc function
                return redirect('hsc', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        print('notvalit')
        form = AdmissionMark()
    return render(request, "postform/diploma.html", {'form': form, 'admission_number': admission_number})

def academic_details(request, admission_number):
    if request.method == 'POST':

        form = academic_Details(request.POST)
        if form.is_valid():
            new_admission_number = generate_unique_admission_number()
            print(new_admission_number)
            date_of_birth = datetime.strptime(request.session['personal_data']['Date_of_Birth'], '%Y-%m-%d').date()
            request.session['personal_data']['Date_of_Birth'] = date_of_birth.isoformat()

            # Create or update the existing instance with address, sslc, and hsc data
            personal_details, created = Personal_Details.objects.update_or_create(
                admissionNo=new_admission_number,
                defaults={
                    **request.session['personal_data'],
                    **request.session['address_data'],
                    **request.session['sslc_data'],
                }
            )

            personal_details.save()
            admissionNo=new_admission_number
            diploma_data = request.session.get('diploma_data', {})
            hsc_data = request.session.get('hsc_data', {})

            if diploma_data:
                Diplomo.objects.create(personal=personal_details, **diploma_data, admissionNo=new_admission_number)

            if hsc_data:
                HSC_Marks.objects.create(personal=personal_details, **hsc_data, admissionNo=new_admission_number)

            Academic_Details.objects.create(personal=personal_details, **form.cleaned_data, admissionNo=new_admission_number)

            personal_data = request.session.get('personal_data', {})
            mode=personal_data['Mode']
            transport = {
                    'admissionNo': admissionNo,
                    "mode":mode
          }

            request.session['transport_data'] = transport
            # Clear session data after saving in the database
            request.session.pop('personal_data', None)
            request.session.pop('address_data', None)
            request.session.pop('sslc_data', None)
            request.session.pop('hsc_data', None)
            request.session.pop('diploma_data', None)
            request.session.pop('file_paths', None)
            return redirect('qrcode')
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = academic_Details()
        personal_data = request.session.get('personal_data', {})
        Quota=personal_data['Quota']
    return render(request, "postform/academic_details.html", {'form': form, 'admission_number': admission_number,"Quota":Quota})



def preview(request):
    personal_data = request.session.get('personal_data', {})
    address_data = request.session.get('address_data', {})
    sslc_data = request.session.get('sslc_data', {})
    hsc_data = request.session.get('hsc_data', {})
    diploma_data = request.session.get('diploma_data', {})
    return render(request, "postform/preview.html", {
        'personal_data': personal_data,
        'address_data': address_data,
        'sslc_data': sslc_data,
        'hsc_data': hsc_data,
        'diploma_data': diploma_data,
    })

def thankyou(request):
# Query the data from your database
    count = Personal_Details.objects.count()
    return render(request, 'test/thankyou.html', {'count': count})

def Aadhaar_Number_exists(Aadhaar_Number):
    # Use filter to check if the admission number exists in the database
    exists = Personal_Details.objects.filter(Aadhaar_Number=Aadhaar_Number).exists()
    return exists

def pdf_check(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    if Aadhaar_Number:
        if Aadhaar_Number_exists(Aadhaar_Number):  # Assuming Aadhaar_Number_exists is a function you've defined
            personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
            admissionNo = personal_details.admissionNo
            admissionFor = personal_details.admissionFor

            hsc_marks = HSC_Marks.objects.filter(admissionNo=admissionNo)
            if hsc_marks:
                hsc_marks = get_object_or_404(HSC_Marks, admissionNo=admissionNo)
                Twelfth_Std_Education_Qualified = hsc_marks.Twelfth_Std_Education_Qualified
            else:
                Twelfth_Std_Education_Qualified=None



            # print(admissionFor,Twelfth_Std_Education_Qualified,'-------------------')
            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "academic":
                return redirect('http://172.16.1.5:8080//fpdf/academic.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "vocational":
                return redirect('http://172.16.1.5:8080//fpdf/vocational.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "II_Year" and Twelfth_Std_Education_Qualified ==None:
                return redirect('http://172.16.1.5:8080//fpdf/diploma.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "II_Year" and Twelfth_Std_Education_Qualified == "academic":
                return redirect('http://172.16.1.5:8080//fpdf/diploma_academic.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "II_Year" and Twelfth_Std_Education_Qualified == "vocational":
                return redirect('http://172.16.1.5:8080//fpdf/diploma_vocational.php?admissionNo={}'.format(admissionNo))

    error_message = "Invalid Aadhaar Number or data not found."
    return render(request, "postform/aadhar_check.html", {'error_message': error_message})


def dashboard_pdf_show(request,Aadhaar_Number):
    if Aadhaar_Number:
        if Aadhaar_Number_exists(Aadhaar_Number):  # Assuming Aadhaar_Number_exists is a function you've defined
            personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
            admissionNo = personal_details.admissionNo
            admissionFor = personal_details.admissionFor

            hsc_marks = HSC_Marks.objects.filter(admissionNo=admissionNo)
            if hsc_marks:
                hsc_marks = get_object_or_404(HSC_Marks, admissionNo=admissionNo)
                Twelfth_Std_Education_Qualified = hsc_marks.Twelfth_Std_Education_Qualified
            else:
                Twelfth_Std_Education_Qualified=None



            # print(admissionFor,Twelfth_Std_Education_Qualified,'-------------------')
            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "academic":
                return redirect('http://172.16.1.5:8080//fpdf/academic.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "vocational":
                return redirect('http://172.16.1.5:8080//fpdf/vocational.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "II_Year" and Twelfth_Std_Education_Qualified ==None:
                return redirect('http://172.16.1.5:8080//fpdf/diploma.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "II_Year" and Twelfth_Std_Education_Qualified == "academic":
                return redirect('http://172.16.1.5:8080//fpdf/diploma_academic.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "II_Year" and Twelfth_Std_Education_Qualified == "vocational":
                return redirect('http://172.16.1.5:8080//fpdf/diploma_vocational.php?admissionNo={}'.format(admissionNo))
            
            return render(request, "postform/error.html", {'error_message': error_message})

    error_message = "Invalid Aadhaar Number or data not found."
    return render(request, "postform/error.html", {'error_message': error_message})

def postform_view(request):

    return render(request, 'postform/view.html')

def certificate_check(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    print(Aadhaar_Number)
    if Aadhaar_Number is not None:
        if Personal_Details.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
            admissionNo = personal_details.admissionNo
            Name = personal_details.Name
            Department = personal_details.Department
            Quota = personal_details.Quota

            personal = certificates.objects.filter(admissionNo=admissionNo)
            hsc = HSC_Marks.objects.filter(admissionNo=admissionNo).first()
            academic=hsc.Twelfth_Std_Education_Qualified
            print(academic)

            if personal:

                personal_details = certificates.objects.get(admissionNo=admissionNo)
                return render(request, "office/recheck.html",{ 'Aadhaar_Number': Aadhaar_Number, 'Name': Name, 'Department': Department, 'Quota': Quota, 'academic': academic,
                'Tenth_mark_sheet': personal_details.Tenth_mark_sheet,
                'eleventh_mark_sheet': personal_details.eleventh_mark_sheet,
                'Twelfth_mark_sheet': personal_details.Twelfth_mark_sheet,
                'Transfer_Certificate': personal_details.Transfer_Certificate,
                'Community_Certificate': personal_details.Community_Certificate,
                'First_year_graduate_Certificate': personal_details.First_year_graduate_Certificate,
                'Income_Certificate': personal_details.Income_Certificate,
                'Migration_Certificate': personal_details.Migration_Certificate})
            else:
                return render(request, "office/form.html", {'Aadhaar_Number': Aadhaar_Number, 'Name': Name, 'Department': Department, 'Quota': Quota,'academic': academic})

    return render(request, "office/index.html")





def office_check(request, Aadhaar_Number):
    personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
    admissionNo = personal_details.admissionNo
    Name = personal_details.Name
    Department = personal_details.Department
    admissionFor = personal_details.admissionFor
    Quota = personal_details.Quota

    if request.method == 'POST':
        form = certificateform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.admissionNo = admissionNo
            user.Name = Name
            user.Department = Department
            user.admissionFor = admissionFor
            user.Quota = Quota

            user.save()
            return render(request, "office/index.html")  # Ensure to create a success.html template
        else:
            return render(request, "postform/error.html", {'form': form, 'Aadhaar_Number': Aadhaar_Number})

    form = certificateform()
    return render(request, "office/form.html", {'form': form, 'Aadhaar_Number': Aadhaar_Number})




def bus_number_check(request):
    # Sample data
    df = pd.read_csv("transport.csv")
    # Create DataFrame
    if request.method == 'POST':
        data = json.loads(request.body)
        Bus_route = data.get('Bus_route')  
        Bus_stop = data.get('Bus_stop')  
        print(Bus_route,Bus_stop,'------------------------')

        if Bus_route:
            BUS_ROUTE = df['BUS ROUTE'].unique().tolist()
            request.session['bus_data'] = {"bus_route":Bus_route}

            filtered_df = df[df['BUS ROUTE'] == Bus_route]

            Bus_stop = filtered_df['Bus Stop'].unique()
            return render(request,"transpoart/transport_submit.html", {'Bus_stop': Bus_stop,"Bus_route":Bus_route,'BUS_ROUTE': BUS_ROUTE})

    # Handle GET request to load school names
    excel_file_path = 'transport.csv'
    try:
        df = pd.read_csv(excel_file_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=['BUS ROUTE'])

    # Extract school names
    BUS_ROUTE = df['BUS ROUTE'].unique().tolist()
    print(BUS_ROUTE)
    return render(request, "transpoart/transport_form.html", {'BUS_ROUTE': BUS_ROUTE})



def bus_root_check(request):
    transport_data=request.session.get('transport_data', {})
    admissionNo=transport_data['admissionNo']
    try:
        df = pd.read_csv("transport.csv")
    except FileNotFoundError:
        return JsonResponse({'error': 'CSV file not found'}, status=404)
    except pd.errors.EmptyDataError:
        return JsonResponse({'error': 'CSV file is empty'}, status=400)
    except pd.errors.ParserError:
        return JsonResponse({'error': 'Error parsing CSV file'}, status=400)

    if request.method == 'POST':
        Bus_route = request.POST.get('Bus_route')
        Bus_stop = request.POST.get('Bus_stop')

        if Bus_route and Bus_stop:
            filtered_df = df[(df['BUS ROUTE'] == Bus_route) & (df['Bus Stop'] == Bus_stop)]
            if not filtered_df.empty:
                time = filtered_df['Time (AM)'].unique()
                busno = filtered_df['BUS NO'].unique()

                form = transportform(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.admissionNo = admissionNo
                    user.Bus_no = busno[0] if busno else None  # Ensuring a single bus number is assigned
                    user.Bus_time = time[0] if time else None  # Ensuring a single bus time is assigned
                    user.save()
                    return render(request, "postform/succes.html", { 'admissionNo': admissionNo,"Bus_no":busno,"Bus_time":time})
                else:
                    return render(request, "postform/error.html", {'form': form, 'errors': form.errors})
            else:
                return render(request, "postform/error.html", {'error': 'No matching bus route or stop found'})
        else:
            return render(request, "postform/error.html", {'error': 'Bus route and stop must be selected'})

    form = transportform()
    return render(request, "transpoart/transport_submit.html", {'form': form})




def save_uploaded_images(file_dict,admission_number):
    profile_images_directory = os.path.join('profile_images',year)
    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        base_file_name = f'{admission_number}_{field_name}_{file_obj.name}'
        file_path = os.path.join(profile_images_directory, base_file_name)

        # Check if the file already exists, if yes, append a number
        counter = 1
        while os.path.exists(file_path):
            new_file_name = f'{field_name}_{counter}_{file_obj.name}'
            file_path = os.path.join(profile_images_directory, new_file_name)
            counter += 1

        with open(file_path, 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        file_paths[field_name] = file_path

    return file_paths



def certificate_dashboard(request):
    certificate = certificates.objects.filter().all()
    return render(request, "test/qr.html",{"certificate":certificate})

def image_check(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    if Aadhaar_Number is not None:
        if  Personal_Details.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            form_update = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
            Name = form_update.Name
            Department = form_update.Department
            Quota = form_update.Quota
            return render(request, "image/image_form.html",{'Aadhaar_Number':Aadhaar_Number,'Name': Name, 'Department': Department, 'Quota': Quota})
    return render(request, "image/check.html")


def save_uploaded_image(file_dict, Aadhaar_Number):
    year = datetime.now().year
    profile_images_directory = os.path.join(settings.MEDIA_ROOT, 'profile_images', str(year), str(Aadhaar_Number))
    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        base_file_name = f'{field_name}_{file_obj.name}'
        file_path = os.path.join(profile_images_directory, base_file_name)

        counter = 1
        while os.path.exists(file_path):
            new_file_name = f'{field_name}_{counter}_{file_obj.name}'
            file_path = os.path.join(profile_images_directory, new_file_name)
            counter += 1

        with open(file_path, 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        file_paths[field_name] = file_path

    return file_paths

def delete_old_image(image_field):
    if image_field:
        image_path = image_field.path
        if os.path.exists(image_path):
            os.remove(image_path)

def image_upload(request, Aadhaar_Number):
    form_update = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
    Name = form_update.Name
    Department = form_update.Department
    Quota = form_update.Quota

    if request.method == 'POST':
        form = image_form(request.POST, request.FILES)
        if form.is_valid():
            file_paths = save_uploaded_image(request.FILES, Aadhaar_Number)

            if 'Profile_Image' in file_paths:
                old_profile_image = form_update.Profile_Image
                form_update.Profile_Image = file_paths.get('Profile_Image')
                delete_old_image(old_profile_image)

            if 'Father_Profile_Image' in file_paths:
                old_father_profile_image = form_update.Father_Profile_Image
                form_update.Father_Profile_Image = file_paths.get('Father_Profile_Image')
                delete_old_image(old_father_profile_image)

            if 'Mother_Profile_Image' in file_paths:
                old_mother_profile_image = form_update.Mother_Profile_Image
                form_update.Mother_Profile_Image = file_paths.get('Mother_Profile_Image')
                delete_old_image(old_mother_profile_image)

            if 'Signature_Image' in file_paths:
                old_signature_image = form_update.Signature_Image
                form_update.Signature_Image = file_paths.get('Signature_Image')
                delete_old_image(old_signature_image)

            form_update.save()

            return render(request, "image/success.html", {'Name': Name, 'Department': Department, 'Quota': Quota})
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = image_form()
    return render(request, "image/image_form.html", {'form': form, 'Aadhaar_Number': Aadhaar_Number})


def qrcode(request):
    transport_data=request.session.get('transport_data', {})
    if transport_data:
        mode=transport_data['mode']
        admissionNo=transport_data['admissionNo']

    print(mode)
    form_update = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    Aadhaar_Number = form_update.Aadhaar_Number
    Profile_Image = form_update.Profile_Image
    Father_Profile_Image =form_update.Father_Profile_Image
    Mother_Profile_Image = form_update.Mother_Profile_Image
    Signature_Image = form_update.Signature_Image
    print(Father_Profile_Image)
    image_url = 'qrcode.png'
    return render(request, "postform/qrcode.html", {
        "Aadhaar_Number":Aadhaar_Number,
        'image_url': image_url,
        'Profile_Image': Profile_Image,
        'Father_Profile_Image': Father_Profile_Image,
        'Mother_Profile_Image': Mother_Profile_Image,
        'Signature_Image': Signature_Image,
        "mode":mode,
    })

