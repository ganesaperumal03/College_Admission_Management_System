from django.shortcuts import render, redirect, get_object_or_404
from .form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details
from .models import Personal_Details, HSC_Marks, Academic_Details
from datetime import datetime

def generate_unique_admission_number():
    count = Personal_Details.objects.count() + 1
    return f"202327{count:02d}"

def postform(request):
    if request.method == 'POST':
        form = AdmissionPersonal(request.POST)
        if form.is_valid():
            # Generate a unique admission number
            admission_number = generate_unique_admission_number()
            # Convert date to string before storing in session
            request.session['personal_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            request.session['personal_data']['Date_of_Birth'] = form.cleaned_data['Date_of_Birth'].isoformat()
            return redirect('address', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = AdmissionPersonal()
    return render(request, "test/personal.html", {'form': form})

def address(request, admission_number):
    if request.method == 'POST':
        form = Admissionaddress(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['address_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            return redirect('sslc', admission_number=admission_number)
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = Admissionaddress()
    return render(request, "test/address.html", {'form': form, 'admission_number': admission_number})

def sslc(request, admission_number):
    if request.method == 'POST':
        form = Admissionsslc(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            request.session['sslc_data'] = {**form.cleaned_data, 'admissionNo': admission_number}
            return redirect('hsc', admission_number=admission_number)
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

def academic_details(request, admission_number):
    if request.method == 'POST':
        form = academic_Details(request.POST)
        if form.is_valid():
            # Convert date to string before storing in session
            date_of_birth = datetime.strptime(request.session['personal_data']['Date_of_Birth'], '%Y-%m-%d').date()
            request.session['personal_data']['Date_of_Birth'] = date_of_birth.isoformat()

            # Try to get an existing instance of Personal_Details
            personal_details, created = Personal_Details.objects.get_or_create(
                admissionNo=request.session['personal_data']['admissionNo'],
                defaults=request.session['personal_data']
            )

            # Update the existing instance with address, sslc, and hsc data
            personal_details.address = request.session.get('address_data', {})
            personal_details.sslc_data = request.session.get('sslc_data', {})
            personal_details.hsc_data = request.session.get('hsc_data', {})
            personal_details.save()

            # Create instances of HSC_Marks and Academic_Details and associate with Personal_Details
            HSC_Marks.objects.create(**request.session['hsc_data'])
            Academic_Details.objects.create(**form.cleaned_data, admissionNo=admission_number)

            # Clear session data after saving in the database
            request.session.pop('personal_data', None)
            request.session.pop('address_data', None)
            request.session.pop('sslc_data', None)
            request.session.pop('hsc_data', None)

            return redirect('thankyou')  # Redirect to the final page
        else:
            return render(request, "postform/error.html", {'form': form})
    else:
        form = academic_Details()
    return render(request, "test/academic_details.html", {'form': form, 'admission_number': admission_number})
def thankyou(request):
    return render(request, "test/thankyou.html")