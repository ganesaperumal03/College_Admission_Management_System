from django.shortcuts import render, redirect, get_object_or_404
from application.form import Perform_sslc, AdmissionPerform, Perform_diploma, Perform_declare, academic_Details,quota_changed,dep_changed,preform_dep_changed,preform_quota_changed
from application.models import Preform, Preform_other_info
from datetime import datetime
import os
from django.core.paginator import Paginator
import base64
from io import BytesIO
from django.http import HttpResponseNotFound
from django.db.models import Q
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
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

from django.contrib.auth.decorators import user_passes_test

def is_allowed_user_dashboard(user):
 
    allowed_emails = ['gmadmin@ritrjpm.ac.in', 'principal@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_userad(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in', 'hodad@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_usercse(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodcse@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_usercivil(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodcivil@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_usereee(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodeee@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_userece(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodece@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_usermech(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodmech@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_userit(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodit@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails

def is_allowed_usercsbs(user):
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodcsbs@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    return user.email in allowed_emails


@user_passes_test(is_allowed_user_dashboard)
def preform_dashboard(request):
    students_info = Preform_other_info.objects.select_related('personal').filter(admission_exit__isnull=True,admissionFor='I_Year',YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(students_info, 10)
    personal_page = request.GET.get('personal_paginator')

    dip_personal_objects = Preform.objects.filter(preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')

    count = Preform.objects.count()

    adcount = Preform_other_info.objects.select_related('personal').filter(admission_exit__isnull=True,personal__Department='B.TECH AD').count()
    sizes = [adcount, 120-adcount]
    ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    csecount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E CSE').count()
    sizes = [csecount, 120-csecount]
    cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    csbscount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.TECH CSBS').count()
    sizes = [csbscount, 60-csbscount]
    csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    civilcount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E CIVIL').count()
    sizes = [civilcount, 60-civilcount]
    civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    eeecount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E EEE').count()
    sizes = [eeecount, 60-eeecount]
    eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    ececount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E ECE').count()
    sizes = [ececount, 120-ececount]
    ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    mechcount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E MECH').count()
    sizes = [mechcount, 60-mechcount]
    mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    itcount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.TECH IT').count()
    sizes = [itcount, 60-itcount]
    it = generate_pie_chart(sizes,25,50,'B.TECH IT')


    dip_adcount = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_adcount, 120-dip_adcount]
    dip_ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    dip_csecount = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_csecount, 120-dip_csecount]
    dip_cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    dip_csbscount = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_csbscount, 60-dip_csbscount]
    dip_csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    dip_civilcount = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_civilcount, 60-dip_civilcount]
    dip_civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    dip_eeecount = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_eeecount, 60-dip_eeecount]
    dip_eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    dip_ececount = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_ececount, 120-dip_ececount]
    dip_ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    dip_mechcount = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_mechcount, 60-dip_mechcount]
    dip_mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    dip_itcount = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_itcount, 60-dip_itcount]
    dip_it = generate_pie_chart(sizes,25,50,'B.TECH IT')

    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
        dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)

    total = Preform.objects.count()
    admitted = Preform.objects.filter(preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()

    return render(request, "preform_dashboard/dashboard.html", {'personal': personal,'total':total,'admitted':admitted,'gq':gq,'mq':mq,'dip_personal': dip_personal,'ad': ad,'civil': civil,'cse': cse,'csbs': csbs,'eee': eee,'ece': ece,'mech': mech,'it': it,'dip_ad': dip_ad,'dip_civil': dip_civil,'dip_cse': dip_cse,'dip_csbs': dip_csbs,'dip_eee': dip_eee,'dip_ece': dip_ece,'dip_mech': dip_mech,'dip_it': dip_it})




@user_passes_test(is_allowed_userad)

def preform_ad(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.TECH AD',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/ad.html", {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


@user_passes_test(is_allowed_usercse)
def preform_cse(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.E CSE',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E CSE',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/cse.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


@user_passes_test(is_allowed_usercivil)
def preform_civil(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.E CIVIL',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E CIVIL',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
   
    return render(request, "preform_dashboard/civil.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


@user_passes_test(is_allowed_userece)
def preform_ece(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.E ECE',admission_exit__isnull=True,admissionFor='I_Year',YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E ECE',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/ece.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


@user_passes_test(is_allowed_usereee)
def preform_eee(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.E EEE',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E EEE',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/eee.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


@user_passes_test(is_allowed_usermech)
def preform_mech(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.E MECH',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E MECH',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/mech.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})



@user_passes_test(is_allowed_userit)
def preform_it(request):
    personal_objects = Preform_other_info.objects.select_related('personal').filter(personal__Department='B.TECH IT',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.TECH IT',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/it.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


@user_passes_test(is_allowed_usercsbs)
def preform_csbs(request):
    personal_objects =Preform_other_info.objects.select_related('personal').filter(personal__Department='B.TECH CSBS',admission_exit__isnull=True,admissionFor='I_Year' ,YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y")))
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.TECH CSBS',preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True,preform_other_info__YEAR_OF_ADMISSION  = int(datetime.now().strftime("%Y"))).count()
    return render(request, "preform_dashboard/csbs.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def preform_data_changed(request, admissionNo):
    new_quota_get = request.GET.get('Quota')
    new_dep_get = request.GET.get('Department')
    personal = get_object_or_404(Preform, admissionNo=admissionNo)
    if new_quota_get!= None:
        if request.method == 'GET':
            old_quota = personal.Quota
            form = preform_quota_changed(request.GET,instance=personal)
            if form.is_valid():
                new_quota = new_quota_get
                if new_quota != old_quota:
                    personal.Quota = new_quota
                    form.save()
                return redirect('preform_dashboard')
            else:
                return render(request, "test/error.html", {'form': form})   
    if new_dep_get!= None:
        if request.method == 'GET':
            form = preform_dep_changed(request.GET,instance=personal)
            old_dep = personal.Branch_Preferrence_1
            if form.is_valid():
                new_dep = new_dep_get
                if new_dep != old_dep:
                    personal.Branch_Preferrence_1 = new_dep
                form.save()
                return redirect('preform_dashboard')
            else:
                return render(request, "test/error.html", {'form': form})
    return render(request, "test/error.html")



from django.shortcuts import render
from application.models import Preform, Preform_other_info

def student_info(request):
    # Fetch data from the models
    students_info = Preform_other_info.objects.select_related('personal').all()
    personal_paginator = Paginator(students_info, 10)
    personal_page = request.GET.get('personal_paginator')

    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    # Pass the data to the template
    return render(request, 'preform_dashboard/test.html', {'students_info': personal})

def preform__delete(request, admissionNo):
    personal = get_object_or_404(Preform, admissionNo=admissionNo)

    personal.admission_exit = 'Yes'
    personal.save()

    # Redirect to the dashboard
    return redirect('preform_dashboard')

def preform_update_index(request,admissionNo):
    return render(request, 'preform_dashboard/update/update_index.html', {'admissionNo': admissionNo})

def preform_update(request, admissionNo):
    personal = get_object_or_404(Preform, admissionNo=admissionNo)

    if request.method == 'POST':
        form = AdmissionPerform(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('preform_update_index',admissionNo=admissionNo)
    else:
        form = AdmissionPerform(instance=personal)

    return render(request, 'preform_dashboard/update/personal_update.html', {'form': form})

def preform_sslc_update(request, admissionNo):
    personal = get_object_or_404(Preform_other_info, admissionNo=admissionNo)

    if request.method == 'POST':
        form = Perform_sslc(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('preform_update_index',admissionNo=admissionNo)
    else:
        form = Perform_sslc(instance=personal)

    return render(request, 'preform_dashboard/update/sslc_update.html', {'form': form})

def preform_diploma_update(request, admissionNo):
    personal = get_object_or_404(Preform_other_info, admissionNo=admissionNo)

    if request.method == 'POST':
        form = Perform_diploma(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('preform_update_index',admissionNo=admissionNo)
    else:
        form = Perform_diploma(instance=personal)

    return render(request, 'preform_dashboard/update/diploma_update.html', {'form': form})

def preform_declare_update(request, admissionNo):
    personal = get_object_or_404(Preform, admissionNo=admissionNo)

    if request.method == 'POST':
        form = Perform_declare(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('preform_update_index',admissionNo=admissionNo)
    else:
        form = Perform_declare(instance=personal)

    return render(request, 'preform_dashboard/update/declare_update.html', {'form': form})
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse


from django.http import HttpResponseBadRequest
def pre_export_to_excel(request):
    # Query the data from each model
    personal_details_data = Preform.objects.all().values()
    hsc_marks_data = Preform_other_info.objects.all().values()

    # Create DataFrames for each model
    personal_details_df = pd.DataFrame(personal_details_data)
    hsc_marks_df = pd.DataFrame(hsc_marks_data)

    # Convert datetime columns to timezone-unaware datetimes
    personal_details_df['date'] = personal_details_df['date'].dt.tz_localize(None)
    # Repeat the above line for each datetime column in your DataFrame

    # Merge DataFrames on a common field if there is one, or concatenate them horizontally
    merged_df = pd.concat([personal_details_df, hsc_marks_df], axis=1)

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the merged DataFrame to the response as an Excel file
    merged_df.to_excel(response, index=False)

    return response


def pre_name_search(request):
    student_search_query = request.GET.get('search')

    count = Preform.objects.count()

    adcount = Preform_other_info.objects.select_related('personal').filter(admission_exit__isnull=True,personal__Department='B.TECH AD').count()
    sizes = [adcount, 120-adcount]
    ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    csecount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E CSE').count()
    sizes = [csecount, 120-csecount]
    cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    csbscount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.TECH CSBS').count()
    sizes = [csbscount, 60-csbscount]
    csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    civilcount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E CIVIL').count()
    sizes = [civilcount, 60-civilcount]
    civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    eeecount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E EEE').count()
    sizes = [eeecount, 60-eeecount]
    eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    ececount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E ECE').count()
    sizes = [ececount, 120-ececount]
    ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    mechcount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.E MECH').count()
    sizes = [mechcount, 60-mechcount]
    mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    itcount = Preform_other_info.objects.filter(admissionFor='I_Year',admission_exit__isnull=True,personal__Department='B.TECH IT').count()
    sizes = [itcount, 60-itcount]
    it = generate_pie_chart(sizes,25,50,'B.TECH IT')



    if student_search_query:
        students = Preform_other_info.objects.select_related('personal').filter(Q(personal__Name__icontains=student_search_query),admissionFor='I_Year',admission_exit__isnull=True)
        if students:
            # If results are found, display a "Found" message
            messages.info(request, f'Results found for "{student_search_query}"')
        else:
            # If no results are found, display a "Not Found" message
            messages.warning(request, f'No results found for "{student_search_query}"')
    else:
        students = Preform.objects.all()

    return render(request, 'preform_dashboard/dashboard.html', {'personal': students,'ad': ad,'civil': civil,'cse': cse,'csbs': csbs,'eee': eee,'ece': ece,'mech': mech,'it': it,})

