from django.shortcuts import render, redirect, get_object_or_404
from application.form import AdmissionPersonal, Admissionaddress, Admissionsslc, AdmissionMark, academic_Details,quota_changed,dep_changed,preform_dep_changed,preform_quota_changed
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


def preform_dashboard(request):
    students_info = Preform_other_info.objects.select_related('personal').all()
    personal_paginator = Paginator(students_info, 10)
    personal_page = request.GET.get('personal_paginator')

    dip_personal_objects = Preform.objects.filter(preform_other_info__admissionFor='II_Year',admission_exit__isnull=True)
    dip_personal_paginator = Paginator(dip_personal_objects, 10)
    dip_personal_page = request.GET.get('dip_personal_page')

    count = Preform.objects.count()

    adcount = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [adcount, 120-adcount]
    ad = generate_pie_chart(sizes,25,50,'B.TECH AD')

    csecount = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [csecount, 120-csecount]
    cse = generate_pie_chart(sizes,25,50,'B.E CSE')

    csbscount = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [csbscount, 60-csbscount]
    csbs = generate_pie_chart(sizes,25,50,'B.TECH CSBS')

    civilcount = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [civilcount, 60-civilcount]
    civil = generate_pie_chart(sizes,25,50,'B.E CIVIL')

    eeecount = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [eeecount, 60-eeecount]
    eee = generate_pie_chart(sizes,25,50,'B.E EEE')

    ececount = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [ececount, 120-ececount]
    ece = generate_pie_chart(sizes,25,50,'B.E ECE')

    mechcount = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    sizes = [mechcount, 60-mechcount]
    mech = generate_pie_chart(sizes,25,50,'B.E MECH')

    itcount = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
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
    admitted = Preform.objects.filter(preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    gq = Preform.objects.filter(Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()

    return render(request, "preform_dashboard/dashboard.html", {'personal': personal,'total':total,'admitted':admitted,'gq':gq,'mq':mq,'dip_personal': dip_personal,'ad': ad,'civil': civil,'cse': cse,'csbs': csbs,'eee': eee,'ece': ece,'mech': mech,'it': it,'dip_ad': dip_ad,'dip_civil': dip_civil,'dip_cse': dip_cse,'dip_csbs': dip_csbs,'dip_eee': dip_eee,'dip_ece': dip_ece,'dip_mech': dip_mech,'dip_it': dip_it})





def preform_ad(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.TECH AD',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/ad.html", {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def preform_cse(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E CSE').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E CSE',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/cse.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def preform_civil(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E CIVIL').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E CIVIL',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
   
    return render(request, "preform_dashboard/civil.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def preform_ece(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E ECE').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E ECE',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/ece.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def preform_eee(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E EEE').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E EEE',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/eee.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def preform_mech(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.E MECH').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.E MECH',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/mech.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})



def preform_it(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.TECH IT').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.TECH IT',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/it.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})


def preform_csbs(request):
    personal_objects = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True)
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
    total = Preform.objects.filter(preform_other_info__admissionFor='I_Year',Branch_Preferrence_1='B.TECH CSBS').count()
    gq = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',Quota='GQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    mq = Preform.objects.filter(Branch_Preferrence_1='B.TECH CSBS',Quota='MQ',preform_other_info__admissionFor='I_Year',admission_exit__isnull=True).count()
    return render(request, "preform_dashboard/csbs.html",  {'personal': personal,'total': total,'gq': gq,'mq': mq,'dip_personal':dip_personal})

def preform_data_changed(request, admissionNo):
    new_quota_get = request.GET.get('Quota')
    new_dep_get = request.GET.get('Branch_Preferrence_1')
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
