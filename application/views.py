from django.shortcuts import render, redirect, get_object_or_404
from .form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details
from .models import Personal_Details, HSC_Marks, Academic_Details
from datetime import datetime
import os
from django.core.paginator import Paginator

def generate_unique_admission_number():
    count = Personal_Details.objects.count() + 1
    return f"202327{count:02d}"

def test(request):
    personal = Personal_Details.objects.all()  # Replace 'Customers' with the actual name of your model
    paginator = Paginator(personal, 10)  # Show 10 customers per page

    page = request.GET.get('page')
    Personal = paginator.get_page(page)
    return render(request, "dashboard/index.html", {'Personal': Personal})

def save_uploaded_images(admission_number, file_dict):
    profile_images_directory = os.path.join('media', 'profile_images')

    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        file_path = os.path.join(profile_images_directory, f'{admission_number}_{field_name.name}')
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



import base64
from io import BytesIO
from django.http import HttpResponseNotFound

def display_signature(request):
    try:
        # Step 1: Retrieve the image data from the database
        your_model_instance = Personal_Details.objects.get(admissionNo=20232701)

        # Check if the Signature_Image is set
        if not your_model_instance.Signature_Image:
            return HttpResponseNotFound("Image not found")

        # Step 3: Read the content of the file
        with open(your_model_instance.Signature_Image.path, 'rb') as image_file:
            image_data = image_file.read()

        # Step 4: Convert the image data to base64 encoding
        image_url = base64.b64encode(image_data).decode()

        return render(request, 'test/image.html', {'image_url': f'data:image;base64,{image_url}'})

    except Personal_Details.DoesNotExist:
        return HttpResponseNotFound("Object not found")

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
            HSC_Marks.objects.create(**request.session['hsc_data'])
            Academic_Details.objects.create(**form.cleaned_data, admissionNo=admission_number)

            # Clear session data after saving in the database
            request.session.pop('personal_data', None)
            request.session.pop('address_data', None)
            request.session.pop('sslc_data', None)
            request.session.pop('hsc_data', None)
            request.session.pop('file_paths', None)

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