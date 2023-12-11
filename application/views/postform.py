from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details,AdmissionDiploma
from application.models import Personal_Details, HSC_Marks, Academic_Details,Diplomo
from datetime import datetime
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


def generate_unique_session_admission_number(session, existing_admission_number=None):
    if existing_admission_number:
        # Handle the conflict, e.g., generate a new admission number
        count = Personal_Details.objects.count() + 1
        return f"2024_{count:02d}"

    count = Personal_Details.objects.count() + 1
    return f"202327_{count:02d}"

def index(request,):
    return render(request, "index.html")

def post_index(request):
    Aadhaar_Number = request.GET.get('Aadhaar_Number')
    if Aadhaar_Number is not None:
        return render(request, "test/personal.html",{'Aadhaar_Number':Aadhaar_Number})
    return render(request, "test/index.html")

def save_uploaded_images(admission_number, file_dict):
    profile_images_directory = os.path.join( 'profile_images')

    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        file_path = os.path.join(profile_images_directory, f'{admission_number}_{field_name}_{file_obj.name}')
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
            file_paths = save_uploaded_images(admission_number, request.FILES)
            
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
            request.session['personal_data']['admissionNo'] = admission_number
            request.session['personal_data']['Date_of_Birth'] = form.cleaned_data['Date_of_Birth'].isoformat()
            admissionFor = form.cleaned_data['admissionFor']
            return redirect('address', admission_number=admission_number, admissionFor=admissionFor)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionPersonal()
    return render(request, "test/personal.html", {'form': form})

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
            request.session['address_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            return redirect('sslc', admission_number=admission_number, admissionFor=admissionFor)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = Admissionaddress()
    return render(request, "test/address.html", {'form': form, 'admission_number': admission_number,'district':district,'TALUK':TALUK})

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
            request.session['sslc_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
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
    return render(request, "test/sslc.html", {'form': form, 'admission_number': admission_number,'school_names':school_names})


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
            request.session['hsc_data'] = {**form.cleaned_data, 'admissionNo': admission_number,}
            return redirect('academic_details', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionMark()
    return render(request, "test/hsc.html", {'form': form, 'admission_number': admission_number,'school_names':school_names})

def diploma(request, admission_number):
    if request.method == 'POST':
        form = AdmissionDiploma(request.POST)
        if form.is_valid():
            request.session['diploma_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
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
    return render(request, "test/diploma.html", {'form': form, 'admission_number': admission_number})

def academic_details(request, admission_number):

    if request.method == 'POST':
        form = academic_Details(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            date_of_birth = datetime.strptime(request.session['personal_data']['Date_of_Birth'], '%Y-%m-%d').date()
            request.session['personal_data']['Date_of_Birth'] = date_of_birth.isoformat()

            # Create or update the existing instance with address, sslc, and hsc data
            personal_details, created = Personal_Details.objects.update_or_create(
                admissionNo=admission_number,
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
                Diplomo.objects.create(personal=personal_details, **diploma_data)

            if hsc_data:
                HSC_Marks.objects.create(personal=personal_details, **hsc_data)

            # Create the Academic_Details instance and associate it with Personal_Details
            Academic_Details.objects.create(personal=personal_details, **form.cleaned_data, admissionNo=admission_number)

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
    return render(request, "test/academic_details.html", {'form': form, 'admission_number': admission_number})



def thankyou(request):
    return render(request, "test/personal.html")








# dashboard
def deals_list(request):
    personal = Personal_Details.objects.all()  # Replace 'Customers' with the actual name of your model
    paginator = Paginator(personal, 10)  # Show 10 customers per page

    page = request.GET.get('page')
    Personal = paginator.get_page(page)

    return render(request, 'dashboard/index.html', {'Personal': Personal})