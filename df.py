from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details
from application.models import Personal_Details, HSC_Marks, Academic_Details
from datetime import datetime
import os
from django.core.paginator import Paginator

def generate_unique_admission_number():
    count = Personal_Details.objects.count() + 1
    return f"202327{count:02d}"


# Your existing code
def handle_uploaded_file(f, admission_number):
    # Define the destination directory
    destination_dir = 'static/upload'

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Construct the file path using the admission number and file name
    file_path = os.path.join(destination_dir, f"{admission_number}_{f.name}")

    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return file_path

def postform(request):
    if request.method == 'POST':
        form = AdmissionPersonal(request.POST, request.FILES)
        if form.is_valid():
            # Generate a unique admission number
            admission_number = generate_unique_admission_number()

            # Create the 'profile_images' directory if it doesn't exist
            profile_images_directory = os.path.join('media', 'profile_images')  # Adjust the path based on your MEDIA_ROOT
            os.makedirs(profile_images_directory, exist_ok=True)

            # Save the uploaded images to the server and store the file paths in the session
            file_paths = {}
            for field_name, file_obj in request.FILES.items():
                file_path = os.path.join(profile_images_directory, f'{admission_number}_{field_name}_{file_obj.name}')
                with open(file_path, 'wb') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

                # Store the file reference (path or URL) in the session
                file_paths[field_name] = file_path

            # Store the file paths in the session
            request.session['file_paths'] = file_paths

            # Convert date to string before storing in session
            # Exclude file-related fields from the session data
            request.session['personal_data'] = {
                key: value for key, value in form.cleaned_data.items() if key not in ['Profile_Image', 'Father_Profile_Image', 'Mother_Profile_Image', 'Signature_Image']
            }
            request.session['personal_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            request.session['personal_data']['admissionNo'] = admission_number
            request.session['personal_data']['Date_of_Birth'] = form.cleaned_data['Date_of_Birth'].isoformat()
            admissionFor = form.cleaned_data['admissionFor']
            return redirect('address', admission_number=admission_number, admissionFor=admissionFor,Profile_Image=Profile_Image)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionPersonal()
    return render(request, "test/personal.html", {'form': form})



def address(request, admission_number, admissionFor):
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
    return render(request, "test/address.html", {'form': form, 'admission_number': admission_number})

def sslc(request, admission_number, admissionFor):
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
    return render(request, "test/sslc.html", {'form': form, 'admission_number': admission_number})


def hsc(request, admission_number):
    if request.method == 'POST':
        form = AdmissionMark(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['hsc_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            return redirect('academic_details', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionMark()
    return render(request, "test/hsc.html", {'form': form, 'admission_number': admission_number})

def diploma(request, admission_number):
    if request.method == 'POST':
        form = AdmissionMark(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['diploma_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            return redirect('academic_details', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionMark()
    return render(request, "test/hsc.html", {'form': form, 'admission_number': admission_number})

def academic_details(request, admission_number):
    if request.method == 'POST':
        form = academic_Details(request.POST)
        if form.is_valid():
            # Retrieve or create the Personal_Details instance
            personal_details, created = Personal_Details.objects.update_or_create(
                admissionNo=admission_number,
                defaults={
                    **request.session['personal_data'],
                    **request.session['address_data'],
                    **request.session['sslc_data'],
                }
            )

            # Create the HSC_Marks instance and associate it with Personal_Details
            HSC_Marks.objects.create(personal=personal_details, **request.session['hsc_data'])

            # Create the Academic_Details instance and associate it with Personal_Details
            Academic_Details.objects.create(personal=personal_details, **form.cleaned_data, admissionNo=admission_number)

            # Clear session data after saving in the database
            request.session.pop('personal_data', None)
            request.session.pop('address_data', None)
            request.session.pop('sslc_data', None)

            return redirect('thankyou')  # Redirect to the final page
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = academic_Details()
    return render(request, "test/academic_details.html", {'form': form, 'admission_number': admission_number})


def thankyou(request):
    return render(request, "test/thankyou.html")








# dashboard
def deals_list(request):
    personal = Personal_Details.objects.all()  # Replace 'Customers' with the actual name of your model
    paginator = Paginator(personal, 10)  # Show 10 customers per page

    page = request.GET.get('page')
    Personal = paginator.get_page(page)

    return render(request, 'dashboard/index.html', {'Personal': Personal})