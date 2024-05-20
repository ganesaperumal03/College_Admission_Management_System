def certificate_check(request):
    Aadhaar_Number = request.GET.get('aadhaar')
    print(Aadhaar_Number)
    if Aadhaar_Number is not None:
        if Personal_Details.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
            admissionNo = personal_details.admissionNo
            personal_details = get_object_or_404(certificates, admissionNo=admissionNo)
            context = {
                    'Tenth_mark_sheet': personal_details.Tenth_mark_sheet,
                    'eleventh_mark_sheet': personal_details.eleventh_mark_sheet,
                    'Twelfth_mark_sheet': personal_details.Twelfth_mark_sheet,
                    'Transfer_Certificate': personal_details.Transfer_Certificate,
                    'Community_Certificate': personal_details.Community_Certificate,
                    'First_year_graduate_Certificate': personal_details.First_year_graduate_Certificate,
                    'Income_Certificate': personal_details.Income_Certificate,
                    'Migration_Certificate': personal_details.Migration_Certificate,
                }
            print('-----------------------------------------------------------------')
            return render(request, "office/form.html",context,{'Aadhaar_Number':Aadhaar_Number})
    return render(request, "office/index.html")




def office_check(request, Aadhaar_Number):
    personal_details = get_object_or_404(Personal_Details, Aadhaar_Number=Aadhaar_Number)
    admissionNo = personal_details.admissionNo

    if request.method == 'POST':
        form = certificateform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.admissionNo = admissionNo
            user.save()
            return render(request, "office/index.html")
        else:
            return render(request, "postform/error.html", {'form': form, 'Aadhaar_Number': Aadhaar_Number})

    form = certificateform()
    return render(request, "office/form.html", {'form': form, 'Aadhaar_Number': Aadhaar_Number})