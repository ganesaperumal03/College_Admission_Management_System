from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPerform,Perform_sslc,Perform_declare,Perform_diploma
from application.models import Personal_Details, HSC_Marks, Academic_Details,Diplomo,Preform_other_info,Preform
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
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def preform_login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            email = User.objects.get(username=username).email
            # Check user's email address and redirect accordingly
            if 'gmadmin@ritrjpm.ac.in' in email:
                return redirect('preform_dashboard')
            elif 'principal@ritrjpm.ac.in' in email:
                return redirect('preform_dashboard')
            elif 'ayyachamy@ritrjpm.ac.in' in email:
                return redirect('preform_dashboard')
            elif 'hodad@ritrjpm.ac.in' in email:
                return redirect('preform_ad')
            elif 'hodcse@ritrjpm.ac.in' in email:
                return redirect('preform_cse')
            elif 'hodcivil@ritrjpm.ac.in' in email:
                return redirect('preform_civil')
            elif 'hodeee@ritrjpm.ac.in' in email:
                return redirect('preform_eee')
            elif 'hodece@ritrjpm.ac.in' in email:
                return redirect('preform_ece')
            elif 'hodmech@ritrjpm.ac.in' in email:
                return redirect('preform_mech')
            elif 'hodit@ritrjpm.ac.in' in email:
                return redirect('preform_it')
            elif 'hodcsbs@ritrjpm.ac.in' in email:
                return redirect('preform_csbs')
            else:
                # Default redirect for users with unrecognized email
                return redirect('default_dashboard')

        else:
            error_message = "Invalid username or password. Please try again."

    return render(request, "sigin/preformlogin.html", {'error_message': error_message})


def generate_unique_admission_number():
    current_year_last_two_digits = datetime.now().strftime("%y")
    add_digit = int(current_year_last_two_digits) + 4
    count = Preform.objects.count() + 1
    return f"{current_year_last_two_digits}{add_digit:02d}{count:03d}"

year = datetime.now().strftime("%Y")

def save_uploaded_images(file_dict):
    profile_images_directory = os.path.join('personal_profile_images'+ year)
    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        base_file_name = f'{field_name}_{file_obj.name}'
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

def preform_pesonal(request):
    if request.method == 'POST':
        form = AdmissionPerform(request.POST, request.FILES)
        if form.is_valid():
             # Save the uploaded images to the server and store the file paths in the session
            file_paths = save_uploaded_images(request.FILES)
            # Clear the file-related fields from the form instance to avoid serialization issues
            form.cleaned_data['Profile_Image'] = None

            # Store file paths as strings in the session
            request.session['file_paths'] = {key: str(value) for key, value in file_paths.items()}

            # Convert date to string before storing in session
            request.session['preform_personal'] = {
                key: value for key, value in form.cleaned_data.items() if key not in ['Profile_Image']
            }
            request.session['preform_personal']['Date_of_Birth'] = form.cleaned_data['Date_of_Birth'].isoformat()
            return redirect('preform_hsc')
        else:
            return render(request, "test/error.html", {'form': form})
    else:
        form = AdmissionPerform()
    return render(request, "preform/personal.html", {'form': form})

def preform_hsc(request):
    year = int(datetime.now().strftime("%Y"))
    print(year)
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
        form = Perform_sslc(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['preform_hsc'] = {**form.cleaned_data}
            diploma = form.cleaned_data['admissionFor']
            if diploma == 'I_Year':
                # Redirect to the 1st year address function
                return redirect('preform_declare')
            elif diploma == 'II_Year':
                # Redirect to the 2nd year sslc function
                return redirect('preform_diploma')
        else:
            return render(request, "test/error.html", {'form': form ,'school_names':school_names,'year_of_passing':year_of_passing})
    else:
        form = Perform_sslc()
    return render(request, "preform/hsc.html", {'form': form ,'school_names':school_names,'year_of_passing':year_of_passing,'year':year})

def preform_diploma(request):
    if request.method == 'POST':
        form = Perform_diploma(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['preform_diploma'] = {**form.cleaned_data}
            return redirect('preform_declare')
        else:
            return render(request, "test/error.html", {'form': form})
    else:
        form = Perform_diploma()
    return render(request, "preform/diploma.html")


def preform_declare(request):
    if request.method == 'POST':
        form = Perform_declare(request.POST)
        if form.is_valid():
            # Move the definition of preform_personal to before using it
            preform_personal = request.session.get('preform_personal', {})
            
            new_admission_number = generate_unique_admission_number()
            personal_details, created = Preform.objects.update_or_create(
                admissionNo=new_admission_number,
                defaults={
                    **preform_personal, **form.cleaned_data,
                }
            )
            personal_details.Profile_Image = request.session['file_paths']['Profile_Image']
            personal_details.save()

            # Create instances of HSC_Marks and Academic_Details and associate with Personal_Details
            diploma_data = request.session.get('preform_diploma', {})  # Corrected variable name
            hsc_data = request.session.get('preform_hsc', {})  # Corrected variable name

            if diploma_data:
                Preform_other_info.objects.create(personal=personal_details, **diploma_data, admissionNo=new_admission_number)

            if hsc_data:
                Preform_other_info.objects.create(personal=personal_details, **hsc_data, admissionNo=new_admission_number)

            # Clear session data after saving in the database
            request.session.pop('preform_personal', None)
            request.session.pop('preform_hsc', None)  # Corrected variable name
            request.session.pop('preform_hsc', None)  # Corrected variable name
            request.session.pop('preform_diploma', None)  # Corrected variable name

            return redirect('pre_index')  # Redirect to the final page
        else:
            return render(request, "test/error.html", {'form': form})
    else:
        form = Perform_declare()
    return render(request, "preform/declare.html")


def pre_index(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    if Aadhaar_Number is not None:
        if not Personal_Details.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            return render(request, "preform/personal.html",{'Aadhaar_Number':Aadhaar_Number})
    return render(request, "preform/index.html")

def Aadhaar_Number_exists(Aadhaar_Number):
    # Use filter to check if the admission number exists in the database
    exists = Preform.objects.filter(Aadhaar_Number=Aadhaar_Number).exists()
    return exists

def preform_pdf_check(request):
    error_message = None
    Aadhaar_Number = request.GET.get('aadhaar')
    if Aadhaar_Number_exists(Aadhaar_Number):
        if Aadhaar_Number is not None:
            admissionNo = Preform.objects.get(Aadhaar_Number=Aadhaar_Number).admissionNo
            admissionFor = Preform_other_info.objects.get(admissionNo=admissionNo).admissionFor
            Twelfth_Std_Education_Qualified = Preform_other_info.objects.get(admissionNo=admissionNo).Twelfth_Std_Education_Qualified

            if admissionFor=="I_Year"  and Twelfth_Std_Education_Qualified=="academic":
                return redirect('pre_aca', admissionNo=admissionNo)
    
            if admissionFor=="I_Year"  and Twelfth_Std_Education_Qualified=="vocational":
                return redirect('pre_voc', admissionNo=admissionNo)

            if admissionFor=="II_Year":
                return redirect('post_dip', admissionNo=admissionNo)

            if admissionFor=="II_Year"  and Twelfth_Std_Education_Qualified=="academic":
                return redirect('post_dip_aca', admissionNo=admissionNo)

            if admissionFor=="II_Year"  and Twelfth_Std_Education_Qualified=="vocational":
                return redirect('post_dip_voc', admissionNo=admissionNo)
        else:
            error_message = "Invalid username or password. Please try again."
    return render(request, "preform/aadhar_check.html")