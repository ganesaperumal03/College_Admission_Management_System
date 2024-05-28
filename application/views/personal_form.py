from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonalform,personalformconform
from application.models import Personalform
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
import matplotlib.pyplot as plt
import io
import base64
from django.core.paginator import Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Max


# def generate_unique_admission_number():
#     today = datetime.now().strftime("%d%m%y")
#     latest_admission = Personalform.objects.aggregate(Max('admissionNo'))['admissionNo__max']

#     if latest_admission:
#         if latest_admission.startswith(today):
#             count = int(latest_admission[len(today) + 1:]) + 1
#         else:
#             count = 1
#     else:
#         count = 1

#     return f"{today}_{count:03d}"
def generate_unique_admission_number():
    date = datetime.now().strftime("%d%m%y")
    today = datetime.now()

    # Count the number of admissions for the current day
    latest_admission_count = Personalform.objects.filter(date=today.date()).count()

    return f"{date}_{latest_admission_count + 1:03d}"

def generate_pie_chart(counts, dpi, fontsize, title):
    fig, ax = plt.subplots()
    wedges, text, autotexts = ax.pie(counts, labels=None, autopct='', startangle=90)

    # Display the count values in the center of each pie slice with increased font size
    for autotext, count in zip(autotexts, counts):
        autotext.set_text(str(count))
        autotext.set_fontsize(fontsize)

    ax.axis('equal')
    ax.set_title(title, fontsize=40)  # Add title

    # Save the plot as a BytesIO object with adjusted DPI
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png', dpi=dpi)
    plt.close()

    # Convert the BytesIO object to base64 encoding
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    return image_base64


def personal_form_login(request):
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
                return redirect('personalform_dashboard')
            if 'reception@ritrjpm.ac.in' in email:
                return redirect('reception_dashboard')
            else:
                # Default redirect for users with unrecognized email
                return redirect('personalform_dashboard')
        else:
            error_message = "Invalid username or password. Please try again."

    return render(request, "sigin/personalformlogin.html", {'error_message': error_message})


def personal_form(request):
    if request.method == 'POST':
        form = AdmissionPersonalform(request.POST)
        if form.is_valid():
            new_admission_number = generate_unique_admission_number()
            Personalform.objects.create(**form.cleaned_data, admissionNo=new_admission_number)
            return redirect('index')  # Redirect to the final page
        else:
            return render(request, "test/error.html", {'form': form})
    else:
        form = AdmissionPersonalform()
    return render(request, "form/personal.html", {'form': form})


def personalform_dashboard(request):
    date=datetime.now()

    personal_objects = Personalform.objects.filter(date=date)
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')

    count = Personalform.objects.count()
    date=datetime.now()
    # adcount = Personalform.objects.filter(Department='B.TECH AD',date=date,gm_conform='ok').count()
    # sizes = [adcount, 120-adcount]
    # ad = generate_pie_chart(sizes,25,50,'B.TECH AD')
    # csecount = Personalform.objects.filter(Department='B.E CSE',gm_conform='ok').count()
    # sizes = [csecount, 120-csecount]
    # cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    # csbscount = Personalform.objects.filter(Department='B.TECH CSBS',gm_conform='ok').count()
    # sizes = [csbscount, 60-csbscount]
    # csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    # civilcount = Personalform.objects.filter(Department='B.E CIVIL',gm_conform='ok').count()
    # sizes = [civilcount, 60-civilcount]
    # civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    # eeecount = Personalform.objects.filter(Department='B.E EEE',gm_conform='ok').count()
    # sizes = [eeecount, 60-eeecount]
    # eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    # ececount = Personalform.objects.filter(Department='B.E ECE',gm_conform='ok').count()
    # sizes = [ececount, 120-ececount]
    # ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    # mechcount = Personalform.objects.filter(Department='B.E MECH',gm_conform='ok').count()
    # sizes = [mechcount, 60-mechcount]
    # mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    # itcount = Personalform.objects.filter(Department='B.TECH IT',gm_conform='ok').count()
    # sizes = [itcount, 160-itcount]
    # it = generate_pie_chart(sizes,25,50,'B.TECH IT')


    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)


    today = Personalform.objects.filter(date=date).count()
    total= Personalform.objects.filter().count()
    admitted = Personalform.objects.filter().count()
    gq = Personalform.objects.filter(Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Quota='MQ',gm_conform='ok').count()

    return render(request, "form/dashboard.html", {'personal': personal,'today':today,"total":total,'admitted':admitted,'gq':gq,'mq':mq,})



def personalform_ad(request):
    personal_objects = Personalform.objects.filter(Department='B.TECH AD',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.TECH AD').count()
    gq = Personalform.objects.filter(Department='B.TECH AD',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.TECH AD',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/ad.html", {'personal': personal,'total': total,'gq': gq,'mq': mq})

def personalform_cse(request):
    personal_objects = Personalform.objects.filter(Department='B.E CSE',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    

    total = Personalform.objects.filter(Department='B.E CSE',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.E CSE',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.E CSE',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/cse.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})

def personalform_civil(request):
    personal_objects = Personalform.objects.filter(Department='B.E CIVIL',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.E CIVIL',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.E CIVIL',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.E CIVIL',Quota='MQ',gm_conform='ok').count()
   
    return render(request, "form/civil.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})


def personalform_ece(request):
    personal_objects = Personalform.objects.filter(Department='B.E ECE',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.E ECE',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.E ECE',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.E ECE',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/ece.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})


def personalform_eee(request):
    personal_objects = Personalform.objects.filter(Department='B.E EEE',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.E EEE',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.E EEE',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.E EEE',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/eee.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})


def personalform_mech(request):
    personal_objects = Personalform.objects.filter(Department='B.E MECH',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.E MECH',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.E MECH',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.E MECH',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/mech.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})



def personalform_it(request):
    personal_objects = Personalform.objects.filter(Department='B.TECH IT',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.TECH IT',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.TECH IT',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.TECH IT',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/it.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})


def personalform_csbs(request):
    personal_objects = Personalform.objects.filter(Department='B.TECH CSBS',gm_conform='ok')
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    total = Personalform.objects.filter(Department='B.TECH CSBS',gm_conform='ok').count()
    gq = Personalform.objects.filter(Department='B.TECH CSBS',Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Department='B.TECH CSBS',Quota='MQ',gm_conform='ok').count()
    return render(request, "form/csbs.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq})


from django.http import HttpResponseBadRequest

def gm_conformation(request, admissionNo):
    new_gm_conform = request.GET.get('gm_conform')
    print(new_gm_conform)
    personal = get_object_or_404(Personalform, admissionNo=admissionNo)
    print(personal)
    if request.method == 'GET':
        gm_conform = personal.gm_conform
        print(gm_conform)
        form = personalformconform(request.GET,instance=personal)
        if form.is_valid():
            if new_gm_conform != gm_conform:
                personal.gm_conform = new_gm_conform
                form.save()
            return redirect('personalform_dashboard')
        else:
            return render(request, "postform/error.html", {'form': form})   

    return render(request, "postform/error.html")


def date_filter(request):
    date_filter = request.GET.get('date')
    print(date_filter)
    # adcount = Personalform.objects.filter(Department='B.TECH AD',gm_conform='ok').count()
    # sizes = [adcount, 120-adcount]
    # ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    # csecount = Personalform.objects.filter(Department='B.E CSE',gm_conform='ok').count()
    # sizes = [csecount, 120-csecount]
    # cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    # csbscount = Personalform.objects.filter(Department='B.TECH CSBS',gm_conform='ok').count()
    # sizes = [csbscount, 60-csbscount]
    # csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    # civilcount = Personalform.objects.filter(Department='B.E CIVIL',gm_conform='ok').count()
    # sizes = [civilcount, 60-civilcount]
    # civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    # eeecount = Personalform.objects.filter(Department='B.E EEE',gm_conform='ok').count()
    # sizes = [eeecount, 60-eeecount]
    # eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    # ececount = Personalform.objects.filter(Department='B.E ECE',gm_conform='ok').count()
    # sizes = [ececount, 120-ececount]
    # ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    # mechcount = Personalform.objects.filter(Department='B.E MECH',gm_conform='ok').count()
    # sizes = [mechcount, 60-mechcount]
    # mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    # itcount = Personalform.objects.filter(Department='B.TECH IT',gm_conform='ok').count()
    # sizes = [itcount, 160-itcount]
    # it = generate_pie_chart(sizes,25,50,'B.TECH IT')
    total = Personalform.objects.count()
    admitted = Personalform.objects.filter().count()
    gq = Personalform.objects.filter(Quota='GQ',gm_conform='ok').count()
    mq = Personalform.objects.filter(Quota='MQ',gm_conform='ok').count()

    if date_filter:
        # Filter your model queryset based on the date
        date=datetime.now()

        filtered_objects = Personalform.objects.filter(date=date_filter)
        today = Personalform.objects.filter(date=date_filter).count()
        print(filtered_objects)
    else:
        # If no date is specified, return all objects
        filtered_objects = Personalform.objects.all()

    return render(request, 'form/dashboard.html', {'personal': filtered_objects, "today":today,"date":date_filter,'total':total,'admitted':admitted,'gq':gq,'mq':mq})


def check_form(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    if Aadhaar_Number is not None:
        form = Personalform.objects.filter(Aadhaar_Number=Aadhaar_Number).first()

        if form is None:  # Form not found, render personal.html with Aadhaar_Number
            return render(request, "form/personal.html", {'Aadhaar_Number': Aadhaar_Number})
        else:
            return render(request, "form/recheck_personal.html", {'form': form})

    return render(request, "form/aadhar.html")

def logout(request):
    return render(request, "index.html")


def reception_dashboard(request):
    personal_objects = Personalform.objects.filter()
    personal_paginator = Paginator(personal_objects, 100)
    personal_page = request.GET.get('personal_page')




    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)



    return render(request, "form/reception.html", {'personal': personal})
