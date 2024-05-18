from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.utils import Image
from django.shortcuts import get_object_or_404
from reportlab.lib.utils import ImageReader  # Import ImageReader
from io import BytesIO
from reportlab.lib.utils import ImageReader
from PIL import Image as PilImage
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
from django.shortcuts import get_object_or_404
from application.models import Personal_Details, Personalform,GQ_Fees,MQ_Fees
from PIL import Image, ImageFilter
import os
from django.shortcuts import render, redirect

import base64
from PyPDF2 import PdfFileReader, PdfFileWriter
from django.templatetags.static import static
from django.templatetags.static import static
def add_watermark(input_pdf, output_pdf, watermark_path):
    watermark = PilImage.open(watermark_path)
    watermark = watermark.convert("RGBA")

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page_number in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_number)
        pdf_writer.addPage(page)

        # Create a new canvas to add the watermark
        overlay = PilImage.new("RGBA", watermark.size, (255, 255, 255, 0))
        overlay.paste(watermark, (0, 0), watermark)

        # Merge the overlay with the existing page
        merged = PilImage.alpha_composite(PilImage.new("RGBA", page.cropBox.getSize(), (255, 255, 255, 0)), overlay)

        # Convert the merged image to RGB
        merged = merged.convert("RGB")

        # Save the merged image to a BytesIO object
        merged_bytes = BytesIO()
        merged.save(merged_bytes, format="PDF", resolution=100.0)

        # Add the merged image to the PDF writer
        pdf_writer.getPage(page_number).mergePage(PdfFileReader(merged_bytes).getPage(0))

    with open(output_pdf, "wb") as output:
        pdf_writer.write(output)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
            # Read binary data from the image file
        binary_data = image_file.read()

            # Encode the binary data to Base64
        base64_data = base64.b64encode(binary_data).decode('utf-8')

    return base64_data


def fees_form(request,admissionNo):
    value = request.GET.get('Place')
    print(value)
    if request.method == 'GET' and value is not None:
        return redirect('fees',value,admissionNo)  # Redirect if 'Place' parameter is provided in the URL
    return render(request, "form/fees.html")

def fees(request,value,admissionNo):
    # preform = Preform.objects.get(admissionNo=admissionNo)
    # info = Preform_other_info.objects.get(admissionNo=admissionNo)
    personal_details = get_object_or_404(Personalform, admissionNo=admissionNo)

    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="example.pdf"'
    document = SimpleDocTemplate(buffer, pagesize=letter)

    # Create PDF
    c = canvas.Canvas(buffer, pagesize=A4)
    
    if (personal_details.Department =="B.TECH AD"):
        
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.TECH AD")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.TECH AD")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         

    elif(personal_details.Department =="B.E CIVIL"):
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.E CIVIL")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.E CIVIL")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         


    elif(personal_details.Department =="B.TECH IT"):
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.TECH IT")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.TECH IT")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         

        
    elif(personal_details.Department =="B.TECH CSBS"):
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.TECH CSBS")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.TECH CSBS")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         


    elif(personal_details.Department =="B.E CSE"):
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.E CSE")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.E CSE")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         

        
    elif(personal_details.Department =="B.E EEE"):
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.E EEE")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.E EEE")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         

        
    elif(personal_details.Department =="B.E ECE") :
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.E ECE")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.E ECE")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         

    elif(personal_details.Department =="B.E MECH") :
        if  (personal_details.Quota =="GQ"):
            gq_fees = get_object_or_404(GQ_Fees,Department="B.E MECH")
            Tuition_Fees=gq_fees.Tuition_Fees
            tuition_Fees=gq_fees.Tuition_Fees
            extra_fees=gq_fees.CoExtra_Curricularfees
            extra=gq_fees.CoExtra_Curricularfees
        else:
            mq_fees = get_object_or_404(MQ_Fees,Department="B.E MECH")
            Tuition_Fees=mq_fees.Tuition_Fees
            tuition_Fees=mq_fees.Tuition_Fees
            extra_fees=mq_fees.CoExtra_Curricularfees
            extra=mq_fees.CoExtra_Curricularfees         

                
  
    
    if value=='80000':
        fees=int(value)
    else:
        fees=int(value)+14000
    totalfees=int(tuition_Fees)+int(extra)+5000+15000+5000+fees
    # Set font
    c.rect(10, 483, 570, 290)

    c.setFont('Helvetica-Bold', 19)
    c.drawString(210, 745, personal_details.Quota) 
    c.drawString(242, 755, '_') 
    c.drawString(257, 745,  personal_details.Department) 


    
    c.setFont('Helvetica-Bold', 15)
    c.drawString(30, 705, 'Tuition Fees') 
    c.drawString(335, 705, ':') 
    c.drawString(385, 705, Tuition_Fees) 

    c.drawString(30, 675, 'Co/Extra Curricular fees ') 
    c.drawString(335, 675, ':') 
    c.drawString(385, 675, extra_fees) 
    

    c.drawString(30, 645, 'Development fees') 
    c.drawString(335, 645, ':') 
    c.drawString(385, 645, '  5000') 

    c.drawString(30, 615, 'Learning Materials/Platform,Uniform Fees') 
    c.drawString(335, 615, ':') 
    c.drawString(385, 615, '15000 ') 

    c.drawString(30, 585, 'Caution Deposit (Refundable)') 
    c.drawString(335, 585, ':') 
    c.drawString(385, 585, '  5000') 
    
    if str(value)=="80000":
        c.drawString(30, 555, 'Hostel Fees') 
        c.drawString(335, 555, ':') 
        c.drawString(385, 555, value)
    else:
        c.drawString(30, 555, 'Transport:') 
        c.drawString(335, 555, ':') 
        c.drawString(385, 555, value)
        
        c.drawString(30, 525, 'Lunch Fees:') 
        c.drawString(335, 525, ':') 
        c.drawString(385, 525, '14000')
    
    
    c.drawString(345, 520, '_________________________') 
    
    
    c.drawString(30, 500, 'Total Fees') 
    c.drawString(335, 500, ':') 
    c.drawString(377, 500, str(totalfees)) 

    c.drawString(345, 495, '_________________________') 



















    # c.setFont('Helvetica-Bold', 19)
    # c.drawString(30, 415, 'GQ') 
    # c.drawString(30, 415, '____') 

    
    # c.setFont('Helvetica-Bold', 15)
    # c.drawString(30, 385, 'Tuition Fees') 
    # c.drawString(335, 385, ':') 
    # c.drawString(385, 385, '23000') 

    # c.drawString(30, 355, 'Co/Extra Curricular fees ') 
    # c.drawString(335, 355, ':') 
    # c.drawString(385, 355, '35,000') 
    
    # c.drawString(30, 325, 'Development fees') 
    # c.drawString(335, 325, ':') 
    # c.drawString(385, 325, '5,000') 

    # c.drawString(30, 295, 'Learning Materials/Platform,Uniform Fees') 
    # c.drawString(335, 295, ':') 
    # c.drawString(385, 295, '15,000') 

    # c.drawString(30, 265, 'Caution Deposit (Refundable)') 
    # c.drawString(335, 265, ':') 
    # c.drawString(385, 265, '5,000') 
    
    # c.drawString(30, 235, 'Hostel Fees') 
    # c.drawString(335, 235, ':') 
    # c.drawString(385, 235, '230000') 
    
    
    # c.drawString(345, 221, '_________________________') 
    
    
    # c.drawString(30, 205, 'Total Fees') 
    # c.drawString(335, 205, ':') 
    # c.drawString(385, 205, '2,30000') 

    # c.drawString(345, 197, '_________________________') 

    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response







