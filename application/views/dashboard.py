from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details,quota_changed,dep_changed
from application.models import Personal_Details, HSC_Marks, Academic_Details,Diplomo,Preform
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

import matplotlib.pyplot as plt
import io
import base64
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
def no_auth(request):
    render(request, "dashboard/no_auth.html")

    
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

def dashboard(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['gmadmin@ritrjpm.ac.in', 'principal@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
        
    personal_objects = Personal_Details.objects.filter(admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')

    dip_personal_objects = Personal_Details.objects.filter(admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')

    count = Personal_Details.objects.count()

    adcount = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [adcount, 120-adcount]
    ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    csecount = Personal_Details.objects.filter(Department='B.E CSE',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [csecount, 120-csecount]
    cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    csbscount = Personal_Details.objects.filter(Department='B.TECH CSBS',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [csbscount, 60-csbscount]
    csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    civilcount = Personal_Details.objects.filter(Department='B.E CIVIL',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [civilcount, 60-civilcount]
    civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    eeecount = Personal_Details.objects.filter(Department='B.E EEE',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [eeecount, 60-eeecount]
    eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    ececount = Personal_Details.objects.filter(Department='B.E ECE',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [ececount, 120-ececount]
    ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    mechcount = Personal_Details.objects.filter(Department='B.E MECH',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [mechcount, 60-mechcount]
    mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    itcount = Personal_Details.objects.filter(Department='B.TECH IT',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [itcount, 160-itcount]
    it = generate_pie_chart(sizes,25,50,'B.TECH IT')


    dip_adcount = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_adcount, 120-dip_adcount]
    dip_ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    dip_csecount = Personal_Details.objects.filter(Department='B.E CSE',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_csecount, 120-dip_csecount]
    dip_cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    dip_csbscount = Personal_Details.objects.filter(Department='B.TECH CSBS',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_csbscount, 60-dip_csbscount]
    dip_csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    dip_civilcount = Personal_Details.objects.filter(Department='B.E CIVIL',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_civilcount, 60-dip_civilcount]
    dip_civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    dip_eeecount = Personal_Details.objects.filter(Department='B.E EEE',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_eeecount, 60-dip_eeecount]
    dip_eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    dip_ececount = Personal_Details.objects.filter(Department='B.E ECE',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_ececount, 120-dip_ececount]
    dip_ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    dip_mechcount = Personal_Details.objects.filter(Department='B.E MECH',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_mechcount, 60-dip_mechcount]
    dip_mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    dip_itcount = Personal_Details.objects.filter(Department='B.TECH IT',admissionFor='II_Year',admission_exit__isnull=True).count()
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

    total = Personal_Details.objects.count()
    admitted = Personal_Details.objects.filter(admissionFor='I_Year',admission_exit__isnull=True).count()
    gq = Personal_Details.objects.filter(Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()

    return render(request, "dashboard/dashboard.html", {'personal': personal,'total':total,'admitted':admitted,'gq':gq,'mq':mq,'dip_personal': dip_personal,'ad': ad,'civil': civil,'cse': cse,'csbs': csbs,'eee': eee,'ece': ece,'mech': mech,'it': it,'dip_ad': dip_ad,'dip_civil': dip_civil,'dip_cse': dip_cse,'dip_csbs': dip_csbs,'dip_eee': dip_eee,'dip_ece': dip_ece,'dip_mech': dip_mech,'dip_it': dip_it})



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render



def ad(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in', 'hodad@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)

    dip_personal_objects = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='I_Year',admission_exit__isnull=True).count()
    gq = Personal_Details.objects.filter(Department='B.TECH AD',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.TECH AD',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/ad.html", {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def cse(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodcse@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.E CSE',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    
    dip_personal_objects = Personal_Details.objects.filter(Department='B.E CSE',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.E CSE').count()
    gq = Personal_Details.objects.filter(Department='B.E CSE',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.E CSE',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/cse.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def civil(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodcivil@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.E CIVIL',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Personal_Details.objects.filter(Department='B.E CIVIL',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.E CIVIL').count()
    gq = Personal_Details.objects.filter(Department='B.E CIVIL',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.E CIVIL',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
   
    return render(request, "dashboard/civil.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def ece(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodece@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.E ECE',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Personal_Details.objects.filter(Department='B.E ECE',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.E ECE').count()
    gq = Personal_Details.objects.filter(Department='B.E ECE',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.E ECE',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/ece.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def eee(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodeee@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.E EEE',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Personal_Details.objects.filter(Department='B.E EEE',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.E EEE').count()
    gq = Personal_Details.objects.filter(Department='B.E EEE',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.E EEE',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/eee.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def mech(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodmech@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']
    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.E MECH',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Personal_Details.objects.filter(Department='B.E MECH',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.E MECH').count()
    gq = Personal_Details.objects.filter(Department='B.E MECH',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.E MECH',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/mech.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})



def it(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodit@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.TECH IT',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Personal_Details.objects.filter(Department='B.TECH IT',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.TECH IT').count()
    gq = Personal_Details.objects.filter(Department='B.TECH IT',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.TECH IT',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/it.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def csbs(request):
    userdata = request.session.get('userdata', {})
    email=userdata
    allowed_emails = ['principal@ritrjpm.ac.in', 'gmadmin@ritrjpm.ac.in','hodcsbs@ritrjpm.ac.in','ayyachamy@ritrjpm.ac.in']

    if email not in allowed_emails:
        return render(request, "dashboard/no_auth.html")
    personal_objects = Personal_Details.objects.filter(Department='B.TECH CSBS',admissionFor='I_Year',admission_exit__isnull=True)
    personal_paginator = Paginator(personal_objects, 10)
    personal_page = request.GET.get('personal_page')
    try:
        personal = personal_paginator.page(personal_page)
    except PageNotAnInteger:
        personal = personal_paginator.page(1)
    except EmptyPage:
        personal = personal_paginator.page(personal_paginator.num_pages)
    dip_personal_objects = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')
    try:
        dip_personal = dip_personal_paginator.page(dip_personal_page)
    except PageNotAnInteger:
        dip_personal = dip_personal_paginator.page(1)
    except EmptyPage:
       dip_personal = dip_personal_paginator.page(dip_personal_paginator.num_pages)
    total = Personal_Details.objects.filter(admissionFor='I_Year',Department='B.TECH CSBS').count()
    gq = Personal_Details.objects.filter(Department='B.TECH CSBS',Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Department='B.TECH CSBS',Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "dashboard/csbs.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def update_index(request,admissionNo):
    return redirect('dashboard')


def personal_update(request, admissionNo):
    personal = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    if request.method == 'POST':
        form = AdmissionPersonal(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('update_index',admissionNo=admissionNo)
    else:
        form = AdmissionPersonal(instance=personal)

    return render(request, 'dashboard/update/personal_update.html', {'form': form})

def address_update(request, admissionNo):
    personal = get_object_or_404(Personal_Details, admissionNo=admissionNo)

    if request.method == 'POST':
        form = Admissionaddress(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('update_index',admissionNo=admissionNo)
    else:
        form = Admissionaddress(instance=personal)

    return render(request, 'dashboard/update/address_update.html', {'form': form})

def sslc_update(request, admissionNo):
    personal = get_object_or_404(Personal_Details, admissionNo=admissionNo)

    if request.method == 'POST':
        form = Admissionsslc(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('update_index',admissionNo=admissionNo)
    else:
        form = Admissionsslc(instance=personal)

    return render(request, 'dashboard/update/sslc_update.html', {'form': form})

def hsc_update(request, admissionNo):
    personal = get_object_or_404(HSC_Marks, admissionNo=admissionNo)

    if request.method == 'POST':
        form = AdmissionMark(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('update_index',admissionNo=admissionNo)
    else:
        form = AdmissionMark(instance=personal)

    return render(request, 'dashboard/update/hsc_update.html', {'form': form})

def academic_update(request, admissionNo):
    personal = get_object_or_404(Academic_Details, admissionNo=admissionNo)

    if request.method == 'POST':
        form = academic_Details(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('update_index',admissionNo=admissionNo)
    else:
        form = academic_Details(instance=personal)

    return render(request, 'dashboard/update/academic_update.html', {'form': form})



def name_search(request):
    student_search_query = request.GET.get('search')

    adcount = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [adcount, 120-adcount]
    ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    csecount = Personal_Details.objects.filter(Department='B.E CSE',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [csecount, 120-csecount]
    cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    csbscount = Personal_Details.objects.filter(Department='B.TECH CSBS',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [csbscount, 60-csbscount]
    csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    civilcount = Personal_Details.objects.filter(Department='B.E CIVIL',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [civilcount, 60-civilcount]
    civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    eeecount = Personal_Details.objects.filter(Department='B.E EEE',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [eeecount, 60-eeecount]
    eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    ececount = Personal_Details.objects.filter(Department='B.E ECE',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [ececount, 120-ececount]
    ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    mechcount = Personal_Details.objects.filter(Department='B.E MECH',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [mechcount, 60-mechcount]
    mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    itcount = Personal_Details.objects.filter(Department='B.TECH IT',admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [itcount, 60-itcount]
    it = generate_pie_chart(sizes,25,50,'B.TECH IT')


    total = Personal_Details.objects.count()
    admitted = Personal_Details.objects.filter(admissionFor='I_Year',admission_exit__isnull=True).count()
    gq = Personal_Details.objects.filter(Quota='GQ',admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Personal_Details.objects.filter(Quota='MQ',admissionFor='I_Year',admission_exit__isnull=True).count()

    if student_search_query:
        students = Personal_Details.objects.filter(Q(Name__icontains=student_search_query),admissionFor='I_Year',admission_exit__isnull=True)
        if students:
            # If results are found, display a "Found" message
            messages.info(request, f'Results found for "{student_search_query}"')
        else:
            # If no results are found, display a "Not Found" message
            messages.warning(request, f'No results found for "{student_search_query}"')
    else:
        students = Personal_Details.objects.all()

    return render(request, 'dashboard/dashboard.html', {'personal': students,'ad': ad,'civil': civil,'cse': cse,'csbs': csbs,'eee': eee,'ece': ece,'mech': mech,'it': it,'total':total,'admitted':admitted,'gq':gq,'mq':mq,})


def dip_name_search(request):
    student_search_query = request.GET.get('search')
    dip_adcount = Personal_Details.objects.filter(Department='B.TECH AD',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_adcount, 120-dip_adcount]
    dip_ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    dip_csecount = Personal_Details.objects.filter(Department='B.E CSE',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_csecount, 120-dip_csecount]
    dip_cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    dip_csbscount = Personal_Details.objects.filter(Department='B.TECH CSBS',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_csbscount, 60-dip_csbscount]
    dip_csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    dip_civilcount = Personal_Details.objects.filter(Department='B.E CIVIL',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_civilcount, 60-dip_civilcount]
    dip_civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    dip_eeecount = Personal_Details.objects.filter(Department='B.E EEE',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_eeecount, 60-dip_eeecount]
    dip_eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    dip_ececount = Personal_Details.objects.filter(Department='B.E ECE',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_ececount, 120-dip_ececount]
    dip_ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    dip_mechcount = Personal_Details.objects.filter(Department='B.E MECH',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_mechcount, 60-dip_mechcount]
    dip_mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    dip_itcount = Personal_Details.objects.filter(Department='B.TECH IT',admissionFor='II_Year',admission_exit__isnull=True).count()
    sizes = [dip_itcount, 60-dip_itcount]
    dip_it = generate_pie_chart(sizes,25,50,'B.TECH IT')

    if student_search_query:
        students = Personal_Details.objects.filter(Q(Name__icontains=student_search_query),admissionFor='II_Year',admission_exit__isnull=True)
        if students:
            # If results are found, display a "Found" message
            messages.info(request, f'Results found for "{student_search_query}"')
        else:
            # If no results are found, display a "Not Found" message
            messages.warning(request, f'No results found for "{student_search_query}"')
    else:
        students = Personal_Details.objects.all()

    return render(request, 'dashboard/dashboard.html', {'personal': students,'dip_ad': dip_ad,'dip_civil': dip_civil,'dip_cse': dip_cse,'dip_csbs': dip_csbs,'dip_eee': dip_eee,'dip_ece': dip_ece,'dip_mech': dip_mech,'dip_it': dip_it})

from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse


from django.http import HttpResponseBadRequest

def data_changed(request, admissionNo):
    new_quota_get = request.GET.get('Quota')
    new_dep_get = request.GET.get('Department')
    personal = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    if new_quota_get!= None:
        if request.method == 'GET':
            old_quota = personal.Quota
            form = quota_changed(request.GET,instance=personal)
            if form.is_valid():
                new_quota = new_quota_get
                if new_quota != old_quota:
                    personal.GQ_MQ_Converted = old_quota
                    personal.Quota = new_quota
                    form.save()
                return redirect('dashboard')
            else:
                return render(request, "postform/error.html", {'form': form})   
    if new_dep_get!= None:
        if request.method == 'GET':
            form = dep_changed(request.GET,instance=personal)
            old_dep = personal.Department
            if form.is_valid():
                new_dep = new_dep_get
                if new_dep != old_dep:
                    personal.Dept_Changed = old_dep
                    personal.Department = new_dep
                form.save()
                return redirect('dashboard')
            else:
                return render(request, "postform/error.html", {'form': form})
    return render(request, "postform/error.html")


def export_page(request):
    return render(request, 'dashboard/excel/index.html')


def export_to_personal_excel(request):
    data = Personal_Details.objects.all().values()  # Query the data you want to export
    df = pd.DataFrame(data)  # Create a DataFrame from the data

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response
from django.db.models import ForeignKey

def export_to_excel_colum(request):
    # Get all column names from the Personal_Details model

# Get all field names for Personal_Details excluding ForeignKey fields
    personal_columns = [field.name for field in Preform._meta.get_fields() if not isinstance(field, ForeignKey)]
    # Get all column names from Model1, Model2, Model3, and Model4
    Hsc_columns = [field.name for field in HSC_Marks._meta.get_fields()]
    academic_columns = [field.name for field in Academic_Details._meta.get_fields()]
    diploma_columns = [field.name for field in Diplomo._meta.get_fields()]

    print(personal_columns)
    for_per = range(1, 78)
    for_hsc = range(1, 39)
    for_dip = range(1, 28)
    for_aca = range(1, 28)
    return render(request, 'dashboard/export_page.html', {'personal_columns': personal_columns, 'for_per': for_per,'for_hsc': for_hsc,'for_dip': for_dip,'for_aca': for_aca, 'Hsc_columns': Hsc_columns, 'academic_columns': academic_columns, 'diploma_columns': diploma_columns})

def export_to_excel(request):
    # Query the data from each model
    personal_details_data = Personal_Details.objects.all().values()
    hsc_marks_data = HSC_Marks.objects.all().values()
    academic_details_data = Academic_Details.objects.all().values()
    diploma_data = Diplomo.objects.all().values()

    # Create DataFrames for each model
    personal_details_df = pd.DataFrame(personal_details_data)
    hsc_marks_df = pd.DataFrame(hsc_marks_data)
    academic_details_df = pd.DataFrame(academic_details_data)
    diploma_df = pd.DataFrame(diploma_data)

    # Merge DataFrames on a common field if there is one, or concatenate them horizontally
    merged_df = pd.concat([personal_details_df, hsc_marks_df, academic_details_df, diploma_df], axis=1)

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the merged DataFrame to the response as an Excel file
    merged_df.to_excel(response, index=False)

    return response

import pandas as pd
from django.http import HttpResponse



def export_to_excel_column(request):
    selected_columns_per = [request.POST.get(f'columns_per_{i}') for i in range(1, 11)]
    selected_columns_hsc = [request.POST.get(f'columns_hsc_{i}') for i in range(1, 11)]
    selected_columns_dip = [request.POST.get(f'columns_dip_{i}') for i in range(1, 11)]
    selected_columns_aca = [request.POST.get(f'columns_aca_{i}') for i in range(1, 11)]

    # Filter out None values from the selected columns
    selected_columns_per = list(filter(None, selected_columns_per))
    selected_columns_hsc = list(filter(None, selected_columns_hsc))
    selected_columns_dip = list(filter(None, selected_columns_dip))
    selected_columns_aca = list(filter(None, selected_columns_aca))

    # Get all field names for Personal_Details excluding ForeignKey fields
    personal_columns = [field.name for field in Personal_Details._meta.get_fields() if not isinstance(field, ForeignKey)]

    # Filter out foreign key fields from the selected columns
    selected_columns_per = [col for col in selected_columns_per if col in personal_columns]
    
    # Repeat the above process for other models if needed

    # Query the selected data from the model
    data_per = Personal_Details.objects.values(*selected_columns_per)
    df_per = pd.DataFrame(data_per)

    data_hsc = HSC_Marks.objects.values(*selected_columns_hsc)
    df_hsc = pd.DataFrame(data_hsc)

    data_dip = Diplomo.objects.values(*selected_columns_dip)
    df_dip = pd.DataFrame(data_dip)

    data_aca = Academic_Details.objects.values(*selected_columns_aca)
    df_aca = pd.DataFrame(data_aca)

    # Concatenate DataFrames, excluding empty DataFrames
    data_frames = [df for df in [df_per, df_hsc, df_dip, df_aca] if not df.empty]
    merged_df = pd.concat(data_frames, axis=1)

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the merged DataFrame to the response as an Excel file
    merged_df.to_excel(response, index=False)

    return response

def delete(request, admissionNo):
    personal = get_object_or_404(Personal_Details, admissionNo=admissionNo)

    personal.admission_exit = 'Yes'
    personal.save()

    # Redirect to the dashboard
    return redirect('dashboard')


