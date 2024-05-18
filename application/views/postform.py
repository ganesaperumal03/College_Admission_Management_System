from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details,AdmissionDiploma
from application.models import Personal_Details, HSC_Marks, Academic_Details,Diplomo
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


def generate_unique_admission_number():
    current_year_last_two_digits = datetime.now().strftime("%y")
    add_digit = int(current_year_last_two_digits) + 4
    count = Personal_Details.objects.count() + 1
    return f"{current_year_last_two_digits}{add_digit:02d}{count:03d}"



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
            elif 'principal@ritrjpm.ac.in' in email:
                return redirect('principal_dashboard')
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



# def send_confirmation_email(email):
#     subject = 'Account Confirmation'
#     message = 'Thank you for registering on our site. Your account is now active.'
#     from_email = settings.DEFAULT_FROM_EMAIL
#     recipient_list = [email]
    
#     send_mail(subject, message, from_email, recipient_list)


year = datetime.now().strftime("%Y")


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
def postform(request):
    if request.method == 'POST':
        form = AdmissionPersonal(request.POST, request.FILES)
        if form.is_valid():
            # Generate a unique admission number
            admission_number = generate_unique_admission_number()

            # Save the uploaded images to the server and store the file paths in the session
            file_paths = save_uploaded_images(request.FILES,admission_number)
            
            # Clear the file-related fields from the form instance to avoid serialization issues
            form.cleaned_data['Profile_Image'] = None
            form.cleaned_data['Father_Profile_Image'] = None
            form.cleaned_data['Mother_Profile_Image'] = None
            form.cleaned_data['Signature_Image'] = None

            # Store file paths as strings in the session
            request.session['file_paths'] = {key: str(value) for key, value in file_paths.items()}

            # Convert date to string before storing in session
            request.session['personal_data'] = {
                key: value for key, value in form.cleaned_data.items() if key not in ['Profile_Image', 'Father_Profile_Image', 'Mother_Profile_Image', 'Signature_Image']
            }
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
    return render(request, "postform/sslc.html", {'form': form, 'admission_number': admission_number,'school_names':school_names})


def hsc(request, admission_number):
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
    return render(request, "postform/hsc.html", {'form': form, 'admission_number': admission_number,'school_names':school_names})

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
            # Convert date to string before storing in session
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

            # Save image references in the Personal_Details instance
            personal_details.Profile_Image = request.session['file_paths']['Profile_Image']
            personal_details.Father_Profile_Image = request.session['file_paths']['Father_Profile_Image']
            personal_details.Mother_Profile_Image = request.session['file_paths']['Mother_Profile_Image']
            personal_details.Signature_Image = request.session['file_paths']['Signature_Image']
            personal_details.save()

            # Create instances of HSC_Marks and Academic_Details and associate with Personal_Details
            diploma_data = request.session.get('diploma_data', {})
            hsc_data = request.session.get('hsc_data', {})

            if diploma_data:
                Diplomo.objects.create(personal=personal_details, **diploma_data, admissionNo=new_admission_number)

            if hsc_data:
                HSC_Marks.objects.create(personal=personal_details, **hsc_data, admissionNo=new_admission_number)

            # Create the Academic_Details instance and associate it with Personal_Details
            Academic_Details.objects.create(personal=personal_details, **form.cleaned_data, admissionNo=new_admission_number)

            # Clear session data after saving in the database
            request.session.pop('personal_data', None)
            request.session.pop('address_data', None)
            request.session.pop('sslc_data', None)
            request.session.pop('hsc_data', None)
            request.session.pop('diploma_data', None)
            request.session.pop('file_paths', None)

            return redirect('post_index')  # Redirect to the final page
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

            hsc_marks = get_object_or_404(HSC_Marks, admissionNo=admissionNo)
            Twelfth_Std_Education_Qualified = hsc_marks.Twelfth_Std_Education_Qualified

            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "academic":
                return redirect('http://localhost/fpdf/academic.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "vocational":
                return redirect('http://localhost/fpdf/vocational.php?admissionNo={}'.format(admissionNo))

    error_message = "Invalid Aadhaar Number or data not found."
    return render(request, "postform/aadhar_check.html", {'error_message': error_message})


def dashboard_pdf_show(request,Aadhaar_Number):
    if Aadhaar_Number:
        if Aadhaar_Number_exists(Aadhaar_Number):  # Assuming Aadhaar_Number_exists is a function you've defined
            personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
            admissionNo = personal_details.admissionNo
            admissionFor = personal_details.admissionFor

            hsc_marks = get_object_or_404(HSC_Marks, admissionNo=admissionNo)
            Twelfth_Std_Education_Qualified = hsc_marks.Twelfth_Std_Education_Qualified

            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "academic":
                return redirect('http://localhost/fpdf/academic.php?admissionNo={}'.format(admissionNo))

            if admissionFor == "I_Year" and Twelfth_Std_Education_Qualified == "vocational":
                return redirect('http://localhost/fpdf/vocational.php?admissionNo={}'.format(admissionNo))

    error_message = "Invalid Aadhaar Number or data not found."
    return render(request, "postform/no_auth.html", {'error_message': error_message})

def postform_view(request):

    return render(request, 'postform/view.html')
