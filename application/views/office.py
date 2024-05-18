from django.shortcuts import render, redirect, get_object_or_404
from application.form import certificateform
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



def office_check(request):
    if request.method == 'POST':
        form = certificateform(request.POST)
        if form.is_valid():
            user = form.save()



    return render(request, "office/form.html")