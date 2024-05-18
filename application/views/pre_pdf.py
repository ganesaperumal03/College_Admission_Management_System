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
from application.models import Personal_Details, HSC_Marks, Academic_Details,Diplomo,Preform,Preform_other_info
from PIL import Image, ImageFilter
import os
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


def pre_aca(request,admissionNo):


    preform = Preform.objects.get(admissionNo=admissionNo)
    info = Preform_other_info.objects.get(admissionNo=admissionNo)
  
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="example.pdf"'
    document = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Create PDF
    c = canvas.Canvas(buffer, pagesize=A4)

    # Set font
    c.setFont('Helvetica', 10)


    c.drawCentredString(290, 820, ":: 1 ::")
    c.drawRightString(530, 820, "App No :")
    c.drawRightString(570, 820, str(preform.admissionNo)) 
    # c.drawInlineImage('C:/Users/GANESHAPERUMAL/Pictures/rit/rit/static/images/watermark.png', 10, 590, width=35, height=40)

    # Set the college logo
    # c.drawInlineImage('rit.png', 10, 690, width=35, height=40)

    # Set the header for the form
    c.setFont('Helvetica-Bold', 15)
    c.setFillColorRGB(0,0,0)
    c.drawCentredString(270, 790, "RAMCO INSTITUTE OF TECHNOLOGY")
    
    c.setFont('Helvetica-Bold', 10)
    c.setFillColorRGB(0,0,0)
    c.drawString(140, 765, "Approved by AICTE, New Delhi & Affiliated to Anna University")
    c.drawString(144, 750, "Accredited by NAAC & An ISO 9001:2015 Certified Institution")
    c.drawString(149, 735, "NBA Accredited UG programs: CSE, EEE, ECE and MECH")
    c.drawString(135, 720, "North Venganallur Village, Rajapalayam - 626 117. Virudhunagar Dist.")
    c.drawString(130, 705, "Phone : 04563 233 400, 402; E-mail : rit@ritrjpm.ac.in; www.ritrjpm.ac.in")

    # Creating the photo and other primary details

    c.setFont('Helvetica', 10)

    c.setFillColorRGB(0,0,0)
    if preform.Profile_Image.path :
        image_path = preform.Profile_Image.path  
        base64_encoded_image = image_to_base64(image_path)

        binary_data = base64.b64decode(base64_encoded_image)

        image_file = BytesIO(binary_data)

        img = Image.open(image_file)

        max_width = 120
        max_height = 130

        img = img.resize((max_width, max_height), Image.LANCZOS)
        img_reader = ImageReader(img)

        img_width, img_height = img.size

        c.drawImage(img_reader, 405, 545, width=img_width, height=img_height)
   
    c.rect(405, 545, 120, 130)

    c.setFont('Helvetica-Bold', 15)
    c.drawString(40, 665, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 635, 'Name') 
    c.drawString(155, 635, ':') 
    c.drawString(30, 605, 'Sex ') 
    c.drawString(155, 605, ':') 

    c.drawString(30, 575, 'Date Of Birth ') 
    c.drawString(155, 575, ':') 

    c.drawString(30, 545, 'Aadhaar_Number') 
    c.drawString(155, 545, ':') 

    c.drawString(30, 515, 'Father_name') 
    c.drawString(155, 515, ':') 

    c.drawString(30, 485, 'Residental_Address 1') 
    c.drawString(155, 485, ':') 

    c.drawString(30, 455, 'Residental_Address 2') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Community') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Occupation') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Self_Email_ID') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Self_Mobile_Number') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Father Mobile Number') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nationality') 
    c.drawString(155, 275, ':') 



    c.drawString(330, 365, 'Physically_Challenged') 
    c.drawString(470, 365, ':') 

    c.drawString(330, 335, 'First_Generation_Graduate') 
    c.drawString(470, 335, ':') 

    c.setFont('Helvetica', 10)
    c.drawString(180, 635, preform.Name) 
    c.drawString(180, 605, preform.Gender) 
    c.drawString(180, 575, str(preform.Date_of_Birth))
    c.drawString(180, 545, preform.Aadhaar_Number) 
    c.drawString(180, 515, preform.Father_name) 
    c.drawString(180, 485, str(preform.Residental_Address_Line_1)) 
    c.drawString(180, 455, preform.Residental_Address_Line_2) 
    c.drawString(180, 425, preform.Community) 
    c.drawString(180, 395, str(preform.Occupation))
    c.drawString(180, 365, str(preform.Self_Email_ID)) 

    c.drawString(180, 275, preform.Nationality) 
    c.drawString(490, 365, preform.Physically_Challenged)
    c.drawString(180, 335, preform.Self_Mobile_Number)
    c.drawString(180, 305, preform.Father_Mobile_Number)




    c.drawString(180, 275, preform.Nationality) 
    c.drawString(490, 365, preform.Physically_Challenged) 
    c.drawString(490, 335, preform.First_Generation_Graduate) 
    c.rect(30, 210, 550, 30)
    c.rect(30, 150, 550, 60)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 219, '10th Std. School Information')
    c.drawString(35, 187, 'Name of the Institution :')
    c.drawString(435, 187, 'Year Of Passing :')
    c.drawString(35, 157, 'Place of the Institution :')
    c.drawString(235, 157, 'Board of Study :')
    c.drawString(435, 157, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 187, info.Tenth_Std_School_Name)
    c.drawString(525, 187, str(info.Tenth_Std_Year_of_Passing))
    c.drawString(150, 157, info.Tenth_Std_Place_of_School)
    c.drawString(315, 157, info.Tenth_Std_School_Type)
    c.drawString(525, 157, info.Tenth_Std_Medium_of_Study)



    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 102, '12th Std. School Information')
    c.drawString(35, 72, 'Name of the Institution :')
    c.drawString(435, 72, 'Year Of Passing :')
    c.drawString(35, 42, 'Place of the Institution :')
    c.drawString(235, 42, 'Category :')
    c.drawString(435, 42, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 72, info.Twelfth_Std_School_Name)
    c.drawString(525, 72, str(info.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 42, info.Twelfth_Std_Place_of_School)
    c.drawString(285, 42, info.Twelfth_Std_Education_Qualified)
    c.drawString(525, 42, info.Twelfth_Std_Medium_of_Study)
    c.rect(30, 90, 550, 30)
    c.rect(30, 30, 550, 60)


    c.showPage()

    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.setFont('Helvetica-Bold', 10)

    c.rect(30, 763, 550, 30)
    c.rect(30, 500, 550, 263)
    c.line(290, 793, 290, 500)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(70, 775, 'HSC Marks Scored in HSC Academic ')
    c.drawString(70, 745, 'Language')
    c.drawString(70, 715, 'English')
    c.drawString(70, 685, 'Mathematics')
    c.drawString(70, 655, 'Physics')
    c.drawString(70, 625, 'Chemistry')
    c.drawString(70, 595, 'Biology')
    c.drawString(70, 565, 'Total')
    c.drawString(70, 535, 'Cutoff')
    c.drawString(70, 505, 'Percentage')
    c.drawString(140, 745, ':')
    c.drawString(140, 715, ':')
    c.drawString(140, 685, ':')
    c.drawString(140, 655, ':')
    c.drawString(140, 625, ':')
    c.drawString(140, 595, ':')
    c.drawString(140, 565, ':')
    c.drawString(140, 535, ':')
    c.drawString(140, 505, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, str(info.Twelfth_Std_aca_Language_Mark))
    c.drawString(150, 715, str(info.Twelfth_Std_aca_English_Mark))
    c.drawString(150, 685, str(info.Twelfth_Std_aca_Mathematics_Mark))
    c.drawString(150, 655, str(info.Twelfth_Std_aca_Physics_Mark))
    c.drawString(150, 625, str(info.Twelfth_Std_aca_Chemistry_Mark))
    c.drawString(150, 595, str(info.Twelfth_Std_aca_Elective_Mark))
    c.drawString(150, 565, str(info.Twelfth_Std_aca_Total_Marks))
    c.drawString(150, 535, str(info.Twelfth_Std_aca_Elective_Mark))
    c.drawString(150, 505, str(info.Twelfth_Std_aca_Total_Marks))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(360, 775, 'Branch (Course) preferred')
    c.drawString(360, 745, 'B.TECH AD')
    c.drawString(360, 715, 'B.E CIVIL')
    c.drawString(360, 685, 'B.TECH CSBS')
    c.drawString(360, 655, 'B.E CSE')
    c.drawString(360, 625, 'B.E EEE')
    c.drawString(360, 595, 'B.E ECE')
    c.drawString(360, 565, 'B.TECH IT')
    c.drawString(360, 535, 'B.E MECH')

    c.drawString(450, 745, ':')
    c.drawString(450, 715, ':')
    c.drawString(450, 685, ':')
    c.drawString(450, 655, ':')
    c.drawString(450, 625, ':')
    c.drawString(450, 595, ':')
    c.drawString(450, 565, ':')
    c.drawString(450, 565, ':')
    c.drawString(450, 535, ':')

    c.setFont('Helvetica', 10)
    c.drawString(490, 745, str(preform.ad_preferrence))
    c.drawString(490, 715, str(preform.civil_preferrence))
    c.drawString(490, 685, str(preform.csbs_preferrence))
    c.drawString(490, 655, str(preform.cse_preferrence))
    c.drawString(490, 625, str(preform.eee_preferrence))
    c.drawString(490, 595, str(preform.ece_preferrence))
    c.drawString(490, 565, str(preform.it_preferrence))
    c.drawString(490, 535, str(preform.mech_preferrence))

    c.setFont('Helvetica', 10)



    c.drawString(30, 440, 'Enclosed Application processing fee in the form of  DD. No./UTR No.-------------------------------------- for Rs.500/-')
    c.drawString(350, 443, str(preform.UPI_Ref_No))    
    c.drawString(30, 410, 'drawn in favour of Ramco Institute of Technology, payable at Rajapalayam')
    c.drawString(30, 370, 'Signature of Candidate: __________________                                                     Signature of Parent: _____________________')
    c.rect(30, 153, 550, 170)

    c.setFont('Helvetica-Bold', 13)

    c.drawString(240, 297, 'FOR OFFICE USE ONLY')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 263, 'ADMISSION NO. :')
    c.drawString(230, 263, 'BRANCH allotted :')
    c.drawString(420, 263, 'Quota allotted :')

    c.drawString(50, 233, 'HOSTEL allotted:')
    c.drawString(420, 233, 'DATE  :')

    c.drawString(50, 173, 'Signature of Admission Incharge')
    c.drawString(420, 173, 'Signature of Principal')


    c.setFont('Helvetica', 10)
    
    if preform.ad_preferrence=='1':
        dep='B.TECH AI & DS'
    elif preform.civil_preferrence=="1":
        dep='B.E CIVIL'
    elif preform.csbs_preferrence=="1":
        dep='B.TECH CSBS'
    elif preform.cse_preferrence=="1":
        dep='B.E CSE'
    elif preform.eee_preferrence=="1":
        dep='B.E EEE'
    elif preform.ece_preferrence=="1":
        dep='B.E ECE'

    elif preform.it_preferrence=="1":
        dep='B.TECH IT'

    elif preform.mech_preferrence=="1":
        dep='B.E MECH'
    else:
        dep='no'

    c.drawString(140, 263,  str(info.admissionNo))
    c.drawString(320, 263,  dep)
    c.drawString(500, 263,  str(preform.Quota))
    c.drawString(140, 233,  str(preform.Hostel_Required))
    c.drawString(460, 233,  str(preform.date))
   

    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response













def pre_voc(request,admissionNo):
    preform = Preform.objects.get(admissionNo=admissionNo)
    info = Preform_other_info.objects.get(admissionNo=admissionNo)
  
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="example.pdf"'
    document = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Create PDF
    c = canvas.Canvas(buffer, pagesize=A4)

    # Set font
    c.setFont('Helvetica', 10)


    c.drawCentredString(290, 820, ":: 1 ::")
    c.drawRightString(530, 820, "App No :")
    c.drawRightString(570, 820, str(preform.admissionNo)) 
    # c.drawInlineImage('C:/Users/GANESHAPERUMAL/Pictures/rit/rit/static/images/watermark.png', 10, 590, width=35, height=40)

    # Set the college logo
    # c.drawInlineImage('rit.png', 10, 690, width=35, height=40)

    # Set the header for the form
    c.setFont('Helvetica-Bold', 15)
    c.setFillColorRGB(0,0,0)
    c.drawCentredString(270, 790, "RAMCO INSTITUTE OF TECHNOLOGY")
    
    c.setFont('Helvetica-Bold', 10)
    c.setFillColorRGB(0,0,0)
    c.drawString(140, 765, "Approved by AICTE, New Delhi & Affiliated to Anna University")
    c.drawString(144, 750, "Accredited by NAAC & An ISO 9001:2015 Certified Institution")
    c.drawString(149, 735, "NBA Accredited UG programs: CSE, EEE, ECE and MECH")
    c.drawString(135, 720, "North Venganallur Village, Rajapalayam - 626 117. Virudhunagar Dist.")
    c.drawString(130, 705, "Phone : 04563 233 400, 402; E-mail : rit@ritrjpm.ac.in; www.ritrjpm.ac.in")

    # Creating the photo and other primary details

    c.setFont('Helvetica', 10)

    c.setFillColorRGB(0,0,0)
    if preform.Profile_Image.path :
        image_path = preform.Profile_Image.path  
        base64_encoded_image = image_to_base64(image_path)

        binary_data = base64.b64decode(base64_encoded_image)

        image_file = BytesIO(binary_data)

        img = Image.open(image_file)

        max_width = 120
        max_height = 130

        img = img.resize((max_width, max_height), Image.LANCZOS)
        img_reader = ImageReader(img)

        img_width, img_height = img.size

        c.drawImage(img_reader, 405, 545, width=img_width, height=img_height)
   
    c.rect(405, 545, 120, 130)

    c.setFont('Helvetica-Bold', 15)
    c.drawString(40, 665, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 635, 'Name') 
    c.drawString(155, 635, ':') 
    c.drawString(30, 605, 'Sex ') 
    c.drawString(155, 605, ':') 

    c.drawString(30, 575, 'Date Of Birth ') 
    c.drawString(155, 575, ':') 

    c.drawString(30, 545, 'Aadhaar_Number') 
    c.drawString(155, 545, ':') 

    c.drawString(30, 515, 'Father_name') 
    c.drawString(155, 515, ':') 

    c.drawString(30, 485, 'Residental_Address 1') 
    c.drawString(155, 485, ':') 

    c.drawString(30, 455, 'Residental_Address 2') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Community') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Occupation') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Self_Email_ID') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Self_Mobile_Number') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Father Mobile Number') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nationality') 
    c.drawString(155, 275, ':') 



    c.drawString(330, 365, 'Physically_Challenged') 
    c.drawString(470, 365, ':') 

    c.drawString(330, 335, 'First_Generation_Graduate') 
    c.drawString(470, 335, ':') 

    c.setFont('Helvetica', 10)
    c.drawString(180, 635, preform.Name) 
    c.drawString(180, 605, preform.Gender) 
    c.drawString(180, 575, str(preform.Date_of_Birth))
    c.drawString(180, 545, preform.Aadhaar_Number) 
    c.drawString(180, 515, preform.Father_name) 
    c.drawString(180, 485, str(preform.Residental_Address_Line_1)) 
    c.drawString(180, 455, preform.Residental_Address_Line_2) 
    c.drawString(180, 425, preform.Community) 
    c.drawString(180, 395, str(preform.Occupation))
    c.drawString(180, 365, str(preform.Self_Email_ID)) 

    c.drawString(180, 275, preform.Nationality) 
    c.drawString(490, 365, preform.Physically_Challenged)
    c.drawString(180, 335, preform.Self_Mobile_Number)
    c.drawString(180, 305, preform.Father_Mobile_Number)




    c.drawString(180, 275, preform.Nationality)
    c.drawString(490, 365, preform.Physically_Challenged) 
    c.drawString(490, 335, preform.First_Generation_Graduate) 
    c.rect(30, 210, 550, 30)
    c.rect(30, 150, 550, 60)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 219, '10th Std. School Information')
    c.drawString(35, 187, 'Name of the Institution :')
    c.drawString(435, 187, 'Year Of Passing :')
    c.drawString(35, 157, 'Place of the Institution :')
    c.drawString(235, 157, 'Board of Study :')
    c.drawString(435, 157, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 187, info.Tenth_Std_School_Name)
    c.drawString(525, 187, str(info.Tenth_Std_Year_of_Passing))
    c.drawString(150, 157, info.Tenth_Std_Place_of_School)
    c.drawString(315, 157, info.Tenth_Std_School_Type)
    c.drawString(525, 157, info.Tenth_Std_Medium_of_Study)



    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 102, '12th Std. School Information')
    c.drawString(35, 72, 'Name of the Institution :')
    c.drawString(435, 72, 'Year Of Passing :')
    c.drawString(35, 42, 'Place of the Institution :')
    c.drawString(235, 42, 'Category :')
    c.drawString(435, 42, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 72, info.Twelfth_Std_School_Name)
    c.drawString(525, 72, str(info.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 42, info.Twelfth_Std_Place_of_School)
    c.drawString(285, 42, info.Twelfth_Std_Education_Qualified)
    c.drawString(525, 42, info.Twelfth_Std_Medium_of_Study)
    c.rect(30, 90, 550, 30)
    c.rect(30, 30, 550, 60)


    c.showPage()

    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.setFont('Helvetica-Bold', 10)

    c.rect(30, 763, 550, 30)
    c.rect(30, 500, 550, 263)
    c.line(290, 793, 290, 500)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(70, 775, 'HSC Marks Scored in HSC Vocational ')
    c.drawString(70, 745, 'Language')
    c.drawString(70, 715, 'English')
    c.drawString(70, 685, 'Chemistry')
    c.drawString(70, 655, info.Twelfth_Std_voc_Mathematics_or_Physics_Name)
    c.drawString(70, 625, info.Twelfth_Std_voc_Vocational_Theory_Name)
    c.drawString(70, 595, 'Practical_Name')
    c.drawString(70, 565, 'Total')
    c.drawString(70, 535, 'Cutoff')
    c.drawString(70, 505, 'Percentage')
    c.drawString(140, 745, ':')
    c.drawString(140, 715, ':')
    c.drawString(140, 685, ':')
    c.drawString(140, 655, ':')
    c.drawString(140, 625, ':')
    c.drawString(140, 595, ':')
    c.drawString(140, 565, ':')
    c.drawString(140, 535, ':')
    c.drawString(140, 505, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, str(info.Twelfth_Std_voc_Language_Mark))
    c.drawString(150, 715, str(info.Twelfth_Std_voc_English_Mark))
    c.drawString(150, 685, str(info.Twelfth_Std_voc_chemistry_Mark))
    c.drawString(150, 655, str(info.Twelfth_Std_voc_Mathematics_or_Physics_Mark))
    c.drawString(150, 625, str(info.Twelfth_Std_voc_Vocational_Theory_Mark))
    c.drawString(150, 595, str(info.Twelfth_Std_voc_Practical_Mark))
    c.drawString(150, 565, str(info.Twelfth_Std_voc_Total_Marks))
    c.drawString(150, 535, str(info.Twelfth_Std_voc_CUT_OFF_Mark))
    c.drawString(150, 505, str(info.Twelfth_Std_voc_PCM_Average))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(360, 775, 'Branch (Course) preferred')
    c.drawString(360, 745, 'B.TECH AD')
    c.drawString(360, 715, 'B.E CIVIL')
    c.drawString(360, 685, 'B.TECH CSBS')
    c.drawString(360, 655, 'B.E CSE')
    c.drawString(360, 625, 'B.E EEE')
    c.drawString(360, 595, 'B.E ECE')
    c.drawString(360, 565, 'B.TECH IT')
    c.drawString(360, 535, 'B.E MECH')

    c.drawString(450, 745, ':')
    c.drawString(450, 715, ':')
    c.drawString(450, 685, ':')
    c.drawString(450, 655, ':')
    c.drawString(450, 625, ':')
    c.drawString(450, 595, ':')
    c.drawString(450, 565, ':')
    c.drawString(450, 565, ':')
    c.drawString(450, 535, ':')

    c.setFont('Helvetica', 10)
    c.drawString(490, 745, str(preform.ad_preferrence))
    c.drawString(490, 715, str(preform.civil_preferrence))
    c.drawString(490, 685, str(preform.csbs_preferrence))
    c.drawString(490, 655, str(preform.cse_preferrence))
    c.drawString(490, 625, str(preform.eee_preferrence))
    c.drawString(490, 595, str(preform.ece_preferrence))
    c.drawString(490, 565, str(preform.it_preferrence))
    c.drawString(490, 535, str(preform.mech_preferrence))

    c.setFont('Helvetica', 10)


    c.drawString(30, 440, 'Enclosed Application processing fee in the form of DD. No./UTR No.-------------------------------------- for Rs.500/-')
    c.drawString(350, 443, str(preform.UPI_Ref_No))
    c.drawString(30, 410, 'drawn in favour of Ramco Institute of Technology, payable at Rajapalayam')
    c.drawString(30, 370, 'Signature of Candidate: __________________                                                     Signature of Parent: _____________________')
    c.rect(30, 153, 550, 170)

    c.setFont('Helvetica-Bold', 13)

    c.drawString(240, 297, 'FOR OFFICE USE ONLY')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 263, 'ADMISSION NO. :')
    c.drawString(230, 263, 'BRANCH allotted :')
    c.drawString(420, 263, 'Quota allotted :')

    c.drawString(50, 233, 'HOSTEL allotted:')
    c.drawString(420, 233, 'DATE  :')

    c.drawString(50, 173, 'Signature of Admission Incharge')
    c.drawString(420, 173, 'Signature of Principal')


    c.setFont('Helvetica', 10)
    c.drawString(140, 263,  str(info.admissionNo))
    c.drawString(500, 263,  str(preform.Branch_Preferrence_1))
    c.drawString(320, 263,  str(preform.Quota))
    c.drawString(140, 233,  str(preform.Hostel_Required))
    c.drawString(460, 233,  preform.date)
   

    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response