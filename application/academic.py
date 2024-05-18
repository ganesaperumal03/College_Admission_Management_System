from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import Personal_Details, HSC_Marks, Academic_Details
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
from .models import Personal_Details, HSC_Marks, Academic_Details,Preform,Preform_other_info
from PIL import Image, ImageFilter
import os
import base64
from PyPDF2 import PdfFileReader, PdfFileWriter
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


def create_pdf(request):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=10696633)
    hsc = HSC_Marks.objects.get(admissionNo=10696633)
    academic = Academic_Details.objects.get(admissionNo=10696633)

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
    c.drawRightString(570, 820, str(personal_details.admissionNo)) 
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

   
    c.rect(405, 545, 120, 130)
    # image_path = 'C:/Users/GANESHAPERUMAL/Pictures/rit/rit/static/images/rit.png'

    # if image_path:
    #     base64_encoded_image = image_to_base64(image_path)

    #     binary_data = base64.b64decode(base64_encoded_image)

    #     image_file = BytesIO(binary_data)

    #     img = Image.open(image_file)

    #     max_width = 90
    #     max_height = 120

    #     img = img.resize((max_width, max_height), Image.LANCZOS)
    #     img_reader = ImageReader(img)

    #     img_width, img_height = img.size

    #     c.drawImage(img_reader, 25, 688, width=img_width, height=img_height)
    
    # if personal_details.Profile_Image.path :
    #     image_path = personal_details.Profile_Image.path  
    #     base64_encoded_image = image_to_base64(image_path)

    #     binary_data = base64.b64decode(base64_encoded_image)

    #     image_file = BytesIO(binary_data)

    #     img = Image.open(image_file)

    #     max_width = 90
    #     max_height = 130

    #     img = img.resize((max_width, max_height), Image.LANCZOS)
    #     img_reader = ImageReader(img)

    #     img_width, img_height = img.size

    #     c.drawImage(img_reader, 30, 545, width=img_width, height=img_height)

    # if personal_details.Father_Profile_Image.path  :
    #     image_path = personal_details.Father_Profile_Image.path  
    #     base64_encoded_image = image_to_base64(image_path)

    #     binary_data = base64.b64decode(base64_encoded_image)

    #     image_file = BytesIO(binary_data)

    #     img = Image.open(image_file)

    #     max_width = 90
    #     max_height = 130

    #     img = img.resize((max_width, max_height), Image.LANCZOS)
    #     img_reader = ImageReader(img)

    #     img_width, img_height = img.size

    #     c.drawImage(img_reader, 150, 545, width=img_width, height=img_height)

    #     image_path = personal_details.Mother_Profile_Image.path  
    #     base64_encoded_image = image_to_base64(image_path)

    #     binary_data = base64.b64decode(base64_encoded_image)

    #     image_file = BytesIO(binary_data)

    #     img = Image.open(image_file)

    #     max_width = 90
    #     max_height = 130

    #     img = img.resize((max_width, max_height), Image.LANCZOS)
    #     img_reader = ImageReader(img)

    #     img_width, img_height = img.size

    #     c.drawImage(img_reader, 270, 545, width=img_width, height=img_height)
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

    c.drawString(30, 515, 'Self_Email_ID') 
    c.drawString(155, 515, ':') 

    c.drawString(30, 485, 'Residental_Address 1') 
    c.drawString(155, 485, ':') 

    c.drawString(30, 455, 'Residental_Address 2') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Community') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Occupation') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Community') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Self_Mobile_Number') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Father Mobile Number') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nationality') 
    c.drawString(155, 275, ':') 



    c.drawString(330, 425, 'Self_Email_ID') 
    c.drawString(470, 425, ':') 

    c.drawString(330, 395, 'Aadhaar_Number') 
    c.drawString(470, 395, ':') 


    c.drawString(330, 365, 'Physically_Challenged') 
    c.drawString(470, 365, ':') 

    c.drawString(330, 335, 'First_Generation_Graduate') 
    c.drawString(470, 335, ':') 

    c.setFont('Helvetica', 10)
    c.drawString(180, 635, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 485, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 335, personal_details.Religion) 
    c.drawString(180, 305, personal_details.Mother_Tongue) 
    c.drawString(180, 275, personal_details.Nativity) 
    # c.drawString(180, 245, personal_details.Self_Mobile_Number) 
    # c.drawString(180, 215, personal_details.Self_Mobile_Number) 
    # c.drawString(180, 185, personal_details.Father_name) 
    # c.drawString(180, 155, personal_details.Father_Mobile_Number) 
    # c.drawString(180, 125, personal_details.Mother_name) 
    # c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
    # c.drawString(180, 65, personal_details.Guardian_name) 
    # c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
    c.drawString(490, 425, personal_details.Community) 
    c.drawString(490, 395, personal_details.Caste) 
    c.drawString(490, 365, personal_details.Community) 
    c.drawString(490, 335, personal_details.Caste) 
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
    c.drawString(150, 187, personal_details.Tenth_Std_School_Name)
    c.drawString(525, 187, str(personal_details.Tenth_Std_Year_of_Passing))
    c.drawString(150, 157, personal_details.Tenth_Std_Place_of_School)
    c.drawString(315, 157, personal_details.Tenth_Std_School_Type)
    c.drawString(525, 157, personal_details.Tenth_Std_Medium_of_Study)



    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 102, '12th Std. School Information')
    c.drawString(35, 72, 'Name of the Institution :')
    c.drawString(435, 72, 'Year Of Passing :')
    c.drawString(35, 42, 'Place of the Institution :')
    c.drawString(235, 42, 'Category :')
    c.drawString(435, 42, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 72, hsc.Twelfth_Std_School_Name)
    c.drawString(525, 72, str(hsc.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 42, hsc.Twelfth_Std_Place_of_School)
    c.drawString(285, 42, hsc.Twelfth_Std_Category)
    c.drawString(525, 42, hsc.Twelfth_Std_Medium_of_Study)
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
    c.drawString(150, 745, str(hsc.Twelfth_Std_aca_Language_Mark))
    c.drawString(150, 715, str(hsc.Twelfth_Std_aca_English_Mark))
    c.drawString(150, 685, str(hsc.Twelfth_Std_aca_Mathematics_Mark))
    c.drawString(150, 655, str(hsc.Twelfth_Std_aca_Physics_Mark))
    c.drawString(150, 625, str(hsc.Twelfth_Std_aca_Chemistry_Mark))
    c.drawString(150, 595, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(150, 565, str(hsc.Twelfth_Std_aca_Total_Marks))
    c.drawString(150, 535, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(150, 505, str(hsc.Twelfth_Std_aca_Total_Marks))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(360, 775, 'SSLC Marks Scored in HSC Academic')
    c.drawString(360, 745, 'Tamil')
    c.drawString(360, 715, 'English')
    c.drawString(360, 685, 'Mathematics')
    c.drawString(360, 655, 'Science')
    c.drawString(360, 625, 'Social Science')
    c.drawString(360, 595, 'Other Subject')
    c.drawString(360, 565, 'Total')

    c.drawString(450, 745, ':')
    c.drawString(450, 715, ':')
    c.drawString(450, 685, ':')
    c.drawString(450, 655, ':')
    c.drawString(450, 625, ':')
    c.drawString(450, 595, ':')
    c.drawString(450, 565, ':')

    c.setFont('Helvetica', 10)
    c.drawString(490, 745, str(hsc.Twelfth_Std_aca_Language_Mark))
    c.drawString(490, 715, str(hsc.Twelfth_Std_aca_English_Mark))
    c.drawString(490, 685, str(hsc.Twelfth_Std_aca_Mathematics_Mark))
    c.drawString(490, 655, str(hsc.Twelfth_Std_aca_Physics_Mark))
    c.drawString(490, 625, str(hsc.Twelfth_Std_aca_Chemistry_Mark))
    c.drawString(490, 595, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(490, 565, str(hsc.Twelfth_Std_aca_Total_Marks))

    c.setFont('Helvetica', 10)


    c.drawString(30, 440, 'Enclosed Application processing fee in the form of DD. No.-------------------------------------- dt------------------------------- for Rs.500/-')
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
    c.drawString(140, 263,  str(personal_details.admissionNo))
    c.drawString(500, 263,  str(personal_details.admissionNo))
    c.drawString(320, 263,  str(personal_details.admissionNo))

    c.drawString(140, 233,  str(personal_details.admissionNo))
    c.drawString(500, 233,  str(personal_details.admissionNo))
    c.showPage()



    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

















# def dip(request):
#     # Create an in-memory PDF file
#     personal_details = get_object_or_404(Personal_Details, admissionNo=10696633)
#     hsc = HSC_Marks.objects.get(admissionNo=10696633)
#     academic = Academic_Details.objects.get(admissionNo=10696633)

#     buffer = BytesIO()
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="example.pdf"'
#     document = SimpleDocTemplate(buffer, pagesize=letter)
    
#     # Create PDF
#     c = canvas.Canvas(buffer, pagesize=A4)

#     # Set font
#     c.setFont('Helvetica', 10)


#     c.drawCentredString(290, 820, ":: 1 ::")
#     c.drawRightString(530, 820, "App No :")
#     c.drawRightString(570, 820, str(personal_details.admissionNo)) 
#     # c.drawInlineImage('C:/Users/GANESHAPERUMAL/Pictures/rit/rit/static/images/watermark.png', 10, 590, width=35, height=40)

#     # Set the college logo
#     # c.drawInlineImage('rit.png', 10, 690, width=35, height=40)

#     # Set the header for the form
#     c.setFont('Helvetica-Bold', 15)
#     c.setFillColorRGB(0,0,0)
#     c.drawCentredString(270, 790, "RAMCO INSTITUTE OF TECHNOLOGY")
    
#     c.setFont('Helvetica-Bold', 10)
#     c.setFillColorRGB(0,0,0)
#     c.drawString(140, 765, "Approved by AICTE, New Delhi & Affiliated to Anna University")
#     c.drawString(144, 750, "Accredited by NAAC & An ISO 9001:2015 Certified Institution")
#     c.drawString(149, 735, "NBA Accredited UG programs: CSE, EEE, ECE and MECH")
#     c.drawString(135, 720, "North Venganallur Village, Rajapalayam - 626 117. Virudhunagar Dist.")
#     c.drawString(130, 705, "Phone : 04563 233 400, 402; E-mail : rit@ritrjpm.ac.in; www.ritrjpm.ac.in")

#     # Creating the photo and other primary details

#     c.setFont('Helvetica', 10)

#     c.setFillColorRGB(0,0,0)

   
#     c.rect(405, 545, 120, 130)
#     # image_path = 'C:/Users/GANESHAPERUMAL/Pictures/rit/rit/static/images/rit.png'

#     # if image_path:
#     #     base64_encoded_image = image_to_base64(image_path)

#     #     binary_data = base64.b64decode(base64_encoded_image)

#     #     image_file = BytesIO(binary_data)

#     #     img = Image.open(image_file)

#     #     max_width = 90
#     #     max_height = 120

#     #     img = img.resize((max_width, max_height), Image.LANCZOS)
#     #     img_reader = ImageReader(img)

#     #     img_width, img_height = img.size

#     #     c.drawImage(img_reader, 25, 688, width=img_width, height=img_height)
    
#     # if personal_details.Profile_Image.path :
#     #     image_path = personal_details.Profile_Image.path  
#     #     base64_encoded_image = image_to_base64(image_path)

#     #     binary_data = base64.b64decode(base64_encoded_image)

#     #     image_file = BytesIO(binary_data)

#     #     img = Image.open(image_file)

#     #     max_width = 90
#     #     max_height = 130

#     #     img = img.resize((max_width, max_height), Image.LANCZOS)
#     #     img_reader = ImageReader(img)

#     #     img_width, img_height = img.size

#     #     c.drawImage(img_reader, 30, 545, width=img_width, height=img_height)

#     # if personal_details.Father_Profile_Image.path  :
#     #     image_path = personal_details.Father_Profile_Image.path  
#     #     base64_encoded_image = image_to_base64(image_path)

#     #     binary_data = base64.b64decode(base64_encoded_image)

#     #     image_file = BytesIO(binary_data)

#     #     img = Image.open(image_file)

#     #     max_width = 90
#     #     max_height = 130

#     #     img = img.resize((max_width, max_height), Image.LANCZOS)
#     #     img_reader = ImageReader(img)

#     #     img_width, img_height = img.size

#     #     c.drawImage(img_reader, 150, 545, width=img_width, height=img_height)

#     #     image_path = personal_details.Mother_Profile_Image.path  
#     #     base64_encoded_image = image_to_base64(image_path)

#     #     binary_data = base64.b64decode(base64_encoded_image)

#     #     image_file = BytesIO(binary_data)

#     #     img = Image.open(image_file)

#     #     max_width = 90
#     #     max_height = 130

#     #     img = img.resize((max_width, max_height), Image.LANCZOS)
#     #     img_reader = ImageReader(img)

#     #     img_width, img_height = img.size

#     #     c.drawImage(img_reader, 270, 545, width=img_width, height=img_height)
#     c.setFont('Helvetica-Bold', 15)
#     c.drawString(40, 665, 'I. Personal Details') 

#     c.setFont('Helvetica-Bold', 10)
#     c.drawString(30, 635, 'Name') 
#     c.drawString(155, 635, ':') 
#     c.drawString(30, 605, 'Sex ') 
#     c.drawString(155, 605, ':') 

#     c.drawString(30, 575, 'Date Of Birth ') 
#     c.drawString(155, 575, ':') 

#     c.drawString(30, 545, 'Age') 
#     c.drawString(155, 545, ':') 

#     c.drawString(30, 515, 'Gender') 
#     c.drawString(155, 515, ':') 

#     c.drawString(30, 485, 'Residental_Address 1') 
#     c.drawString(155, 485, ':') 

#     c.drawString(30, 455, 'Residental_Address 2') 
#     c.drawString(155, 455, ':') 

#     c.drawString(30, 425, 'Community') 
#     c.drawString(155, 425, ':') 

#     c.drawString(30, 395, 'Occupation') 
#     c.drawString(155, 395, ':') 

#     c.drawString(30, 365, 'Community') 
#     c.drawString(155, 365, ':') 

#     c.drawString(30, 335, 'Self_Mobile_Number') 
#     c.drawString(155, 335, ':') 

#     c.drawString(30, 305, 'Father Mobile Number') 
#     c.drawString(155, 305, ':') 

#     c.drawString(30, 275, 'Nationality') 
#     c.drawString(155, 275, ':') 



#     c.drawString(330, 425, 'Self_Email_ID') 
#     c.drawString(400, 425, ':') 

#     c.drawString(330, 395, 'Aadhaar_Number') 
#     c.drawString(400, 395, ':') 
#     c.setFont('Helvetica', 10)
#     c.drawString(180, 485, personal_details.Name) 
#     c.drawString(180, 455, personal_details.Gender) 
#     c.drawString(180, 425, str(personal_details.Date_of_Birth))
#     c.drawString(180, 365, personal_details.Nationality) 
#     c.drawString(180, 395, str(personal_details.Age)) 
#     c.drawString(180, 335, personal_details.Religion) 
#     c.drawString(180, 305, personal_details.Mother_Tongue) 
#     c.drawString(180, 275, personal_details.Nativity) 
#     # c.drawString(180, 245, personal_details.Self_Mobile_Number) 
#     # c.drawString(180, 215, personal_details.Self_Mobile_Number) 
#     # c.drawString(180, 185, personal_details.Father_name) 
#     # c.drawString(180, 155, personal_details.Father_Mobile_Number) 
#     # c.drawString(180, 125, personal_details.Mother_name) 
#     # c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
#     # c.drawString(180, 65, personal_details.Guardian_name) 
#     # c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
#     c.drawString(420, 425, personal_details.Community) 
#     c.drawString(420, 395, personal_details.Caste) 
#     c.rect(30, 210, 550, 30)
#     c.rect(30, 150, 550, 60)

#     c.rect(30, 90, 550, 30)
#     c.rect(30, 30, 550, 60)

#     c.showPage()

#     c.drawCentredString(290, 820, ":: 2 ::")
#     c.setFont('Helvetica-Bold', 13)
#     c.setFont('Helvetica-Bold', 10)
#     c.drawString(30, 793, 'diplomo Register Number :')
#     c.drawString(400, 793, 'dip certificate No :')
#     c.drawString(240, 793, 'diplomo Studied In  :')

#     c.drawString(30, 763, 'dip total_percentages:')
#     c.drawString(400, 763, 'dip total_mark:')
#     c.drawString(240, 763, 'dip obtain_mark :')

#     c.setFont('Helvetica', 10)
#     # c.drawString(180, 793, 'diplomo.diploma_register_no')
#     # c.drawString(510, 793, 'diplomo.diploma_certificate_no')
#     # c.drawString(370, 793, 'diplomo.diploma_studied_in')

#     # c.drawString(180, 763, 'diplomo.total_percentages')
#     # c.drawString(510, 763, 'diplomo.diploma_total_mark')
#     # c.drawString(370, 763, 'diplomo.diploma_obtain_mark')
#     c.rect(30, 703, 550, 30)
#     c.rect(30, 523, 550, 180)
#     c.line(290, 733, 290, 523)

#     c.rect(30, 73, 550, 150)

#     c.showPage()



#     c.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)

#     return response