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
from application.models import Personal_Details, HSC_Marks, Academic_Details,Diplomo
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



# .........................................................................post_aca..........................................................



def post_aca(request,admissionNo):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    hsc = HSC_Marks.objects.get(admissionNo=admissionNo)
    academic = Academic_Details.objects.get(admissionNo=admissionNo)

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

    
    c.setFont('Helvetica-Bold', 10)
    c.rect(465, 660, 90, 30)
    c.drawRightString(455, 675, "Application from ")
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.setFont('Helvetica', 10)
    c.drawString(470, 675, personal_details.admissionFor)  
    c.drawString(470, 635, personal_details.Quota)  # Replace with the actual quota
    c.drawString(470, 595, personal_details.Department)  # Replace with the actual branch
    c.drawString(470, 555, personal_details.Mode)  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)
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
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 485, 'Name') 
    c.drawString(155, 485, ':') 
    c.drawString(30, 455, 'Sex ') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Date Of Birth ') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Age') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Nationality') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Religion') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Mother Tounge') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nativity') 
    c.drawString(155, 275, ':') 

    c.drawString(30, 245, 'Self Mobile Number') 
    c.drawString(155, 245, ':') 

    c.drawString(30, 215, 'Self E - Mail ID') 
    c.drawString(155, 215, ':') 

    c.drawString(30, 185, 'Father Name') 
    c.drawString(155, 185, ':') 

    c.drawString(30, 155, 'Father Mobile Number') 
    c.drawString(155, 155, ':') 

    c.drawString(30, 125, 'Mother Name') 
    c.drawString(155, 125, ':') 

    c.drawString(30, 95, 'Mother Mobile Number') 
    c.drawString(155, 95, ':') 

    c.drawString(30, 65, 'Guardian Name') 
    c.drawString(155, 65, ':') 

    c.drawString(30, 35, 'Guardian Mobile Number') 
    c.drawString(155, 35, ':') 

    c.drawString(330, 485, 'Community') 
    c.drawString(400, 485, ':') 

    c.drawString(330, 455, 'Caste') 
    c.drawString(400, 455, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 485, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 335, personal_details.Religion) 
    c.drawString(180, 305, personal_details.Mother_Tongue) 
    c.drawString(180, 275, personal_details.Nativity) 
    c.drawString(180, 245, personal_details.Self_Mobile_Number) 
    c.drawString(180, 215, personal_details.Self_Mobile_Number) 
    c.drawString(180, 185, personal_details.Father_name) 
    c.drawString(180, 155, personal_details.Father_Mobile_Number) 
    c.drawString(180, 125, personal_details.Mother_name) 
    c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
    c.drawString(180, 65, personal_details.Guardian_name) 
    c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
    c.drawString(420, 485, personal_details.Community) 
    c.drawString(420, 455, personal_details.Caste) 




    c.showPage()
    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'II. Communication Details')

    # Draw the rectangle
    c.rect(100, 522, 480, 260)
    c.line(100, 742, 580, 742)  # Horizontal line under the permanent address
    c.line(100, 712, 580, 712)
    c.line(100, 682, 580, 682)
    c.line(100, 652, 580, 652)
    c.line(100, 622, 580, 622)
    c.line(100, 592, 580, 592)
    c.line(100, 562, 580, 562)
    c.line(330, 782, 330, 520)  #   vertical

    # Set the font
    c.setFont('Helvetica-Bold', 13)

    # Place the value inside the rectangle
    c.drawString(130, 755, 'Permanent Address')
    c.drawString(390, 755, 'Communication Address')
    c.setFont('Helvetica', 11)
    c.drawString(170, 725, personal_details.Permanent_Address_Door_No) 
    c.drawString(140, 695, personal_details.Permanent_Address_Street_Name) 
    c.drawString(150, 665, personal_details.Permanent_Address_Location) 
    c.drawString(165, 635, personal_details.Permanent_Address_Pincode) 
    c.drawString(150, 605, personal_details.Permanent_Address_Taluk) 
    c.drawString(150, 575, personal_details.Permanent_Address_District) 
    c.drawString(150, 545, personal_details.Permanent_Address_State) 

    c.drawString(450, 725, personal_details.Communication_Address_Door_No) 
    c.drawString(420, 695, personal_details.Communication_Address_Street_Name) 
    c.drawString(430, 665, personal_details.Communication_Address_Location) 
    c.drawString(445, 635, personal_details.Communication_Address_Pincode) 
    c.drawString(420, 605, personal_details.Communication_Address_Taluk) 
    c.drawString(420, 575, personal_details.Communication_Address_District) 
    c.drawString(420, 545, personal_details.Communication_Address_State) 

    c.drawString(30, 725, 'Door No') 
    c.drawString(30, 695, 'Street Name') 
    c.drawString(30, 665, 'Location ') 
    c.drawString(30, 635, 'Pincode') 
    c.drawString(30, 605, 'Taluk ') 
    c.drawString(30, 575, 'District ') 
    c.drawString(30, 545, 'State') 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 483, 'III. Admission Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 453, '1. Counselling Application Number :')
    c.drawString(350, 453, '2. Management Application Number :')
    c.drawString(30, 423, '3. Counselling General Rank  :')
    c.drawString(350, 423, '4. Counselling Community Rank :')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number :')

    c.setFont('Helvetica', 10)
    c.drawString(230, 453, str(academic.Counselling_Application_No))
    c.drawString(530, 453, 'academic')
    c.drawString(230, 423, str(academic.Counselling_General_Rank))
    c.drawString(530, 423, 'academic')
    c.drawString(230, 393, str(academic.GQ_Admission_Number))
    
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 343, 'IV. Academic Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 313, 'a. EMIS Number')
    c.setFont('Helvetica', 10)
    c.drawString(120, 313, personal_details.EMIS_ID)
    c.rect(30, 263, 550, 30)
    c.rect(30, 203, 550, 60)
    c.rect(30, 120, 550, 30)
    c.rect(30, 60, 550, 60)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 277, '10th Std. School Information')
    c.drawString(35, 247, 'Name of the Institution :')
    c.drawString(435, 247, 'Year Of Passing :')
    c.drawString(35, 217, 'Place of the Institution :')
    c.drawString(235, 217, 'Board of Study :')
    c.drawString(435, 217, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 247, personal_details.Tenth_Std_School_Name)
    c.drawString(525, 247, str(personal_details.Tenth_Std_Year_of_Passing))
    c.drawString(150, 217, personal_details.Tenth_Std_Place_of_School)
    c.drawString(315, 217, personal_details.Tenth_Std_School_Type)
    c.drawString(525, 217, personal_details.Tenth_Std_Medium_of_Study)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 135, '11th Std. School Information')
    c.drawString(35, 103, 'Name of the Institution :')
    c.drawString(435, 103, 'Year Of Passing :')
    c.drawString(35, 71, 'Place of the Institution :')
    c.drawString(235, 71, 'Category :')
    c.drawString(435, 71, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 103, hsc.Eleventh_Std_School_Name)
    c.drawString(525, 103, str(hsc.Eleventh_Std_Year_of_Passing))
    c.drawString(150, 71, hsc.Eleventh_Std_Place_of_School)
    c.drawString(285, 71, hsc.Eleventh_Std_Category)
    c.drawString(525, 71, hsc.Eleventh_Std_Medium_of_Study)
    # Build the PDF document
    # Save the PDF
    c.showPage()
    c.drawCentredString(290, 820, ":: 3 ::")
    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, '12th Std. School Information')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, hsc.Twelfth_Std_School_Name)
    c.drawString(525, 745, str(hsc.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 715, hsc.Twelfth_Std_Place_of_School)
    c.drawString(285, 715, hsc.Twelfth_Std_Category)
    c.drawString(525, 715, hsc.Twelfth_Std_Medium_of_Study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.HSC Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'HSC Register Number :')
    c.drawString(50, 593, 'HSC Marksheet Number :')
    c.drawString(370, 623, 'HSC Studied In  :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, hsc.Twelfth_Std_Register_No)
    c.drawString(180, 593, hsc.Twelfth_Std_Marksheet_No)
    c.drawString(450, 623, hsc.Twelfth_Std_studied_in)


    c.rect(30, 543, 550, 30)
    c.rect(30, 363, 550, 180)
    c.line(290, 365, 290, 545) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 555, 'HSC Marks Scored in HSC Academic ')
    c.drawString(70, 520, 'Language')
    c.drawString(70, 498, 'English')
    c.drawString(70, 473, 'Mathematics')
    c.drawString(70, 448, 'Physics')
    c.drawString(70, 423, 'Chemistry')
    c.drawString(70, 398, 'Biology')
    c.drawString(70, 373, 'Total')
    c.drawString(330, 398, 'Cutoff')
    c.drawString(330, 373, 'Percentage')
    c.drawString(140, 520, ':')
    c.drawString(140, 498, ':')
    c.drawString(140, 473, ':')
    c.drawString(140, 448, ':')
    c.drawString(140, 423, ':')
    c.drawString(140, 398, ':')
    c.drawString(140, 373, ':')
    c.drawString(390, 398, ':')
    c.drawString(390, 373, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 520, str(hsc.Twelfth_Std_aca_Language_Mark))
    c.drawString(150, 498, str(hsc.Twelfth_Std_aca_English_Mark))
    c.drawString(150, 473, str(hsc.Twelfth_Std_aca_Mathematics_Mark))
    c.drawString(150, 448, str(hsc.Twelfth_Std_aca_Physics_Mark))
    c.drawString(150, 423, str(hsc.Twelfth_Std_aca_Chemistry_Mark))
    c.drawString(150, 398, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(150, 373, str(hsc.Twelfth_Std_aca_Total_Marks))
    c.drawString(400, 398, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(400, 373, str(hsc.Twelfth_Std_aca_Total_Marks))
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 333, 'VI. SSLC Details')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 303, 'SSLC Register Number :')
    c.drawString(50, 273, 'SSLC Marksheet Number :')
    c.drawString(370, 303, 'SSLC Studied In :')
    c.drawString(370, 273, 'SSLC Exam Number :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 303, personal_details.Tenth_Std_Register_No)
    c.drawString(180, 273, personal_details.Tenth_Std_Marksheet_No)
    c.drawString(470, 303, personal_details.Tenth_Std_Studied_In)
    c.drawString(470, 273, personal_details.Tenth_Std_Roll_No)

    c.rect(30, 223, 550, 30)
    c.rect(30, 43, 550, 180)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 232, 'SSLC Marks Scored in HSC Academic ')
    c.drawString(215, 207, 'Tamil')
    c.drawString(215, 182, 'English')
    c.drawString(215, 157, 'Mathematics')
    c.drawString(215, 132, 'Science')
    c.drawString(215, 107, 'Social Science ')
    c.drawString(215, 82, 'N/A ')
    c.drawString(215, 57, 'Total')
    c.drawString(300, 207, ':')
    c.drawString(300, 182, ':')
    c.drawString(300, 157, ':')
    c.drawString(300, 132, ':')
    c.drawString(300, 107, ': ')
    c.drawString(300, 82, ':')
    c.drawString(300, 57, ':')
    c.setFont('Helvetica', 10)
    c.drawString(320, 207, str(personal_details.Tenth_Std_Tamil_Mark))
    c.drawString(320, 182, str(personal_details.Tenth_Std_English_Mark))
    c.drawString(320, 157, str(personal_details.Tenth_Std_Maths_Mark))
    c.drawString(320, 132, str(personal_details.Tenth_Std_Science_Mark))
    c.drawString(320, 107, str(personal_details.Tenth_Std_SocialScience_Mark))
    c.drawString(320, 82, str(personal_details.Tenth_Std_Others_Mark))
    c.drawString(320, 57, str(personal_details.Tenth_Std_Obtain_Mark))
    c.showPage()
    c.drawCentredString(290, 820, ":: 4 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 790, 'V. Special Reservation Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 760, '1.Ex-Service Man Quota ') 
    c.drawString(30, 730, '2.Sports Quota ') 
    c.drawString(30, 700, '3.Differently abled Person Quota ') 
    c.drawString(30, 670, '4.PMSS (only SC/ST/SCA/SCC) ') 
    c.drawString(30, 640, '5.First Generation Graduate') 
    c.drawString(30, 610, '6.Certificate Number') 
    c.drawString(30, 580, "7.7.5% Govt. Quota") 
    c.drawString(30, 550, '8.Vocational') 

    c.drawString(200, 760, ':') 
    c.drawString(200, 730, ':') 
    c.drawString(200, 700, ':') 
    c.drawString(200, 670, ':') 
    c.drawString(200, 640, ':') 
    c.drawString(200, 610, ':') 
    c.drawString(200, 580, ':') 
    c.drawString(200, 550, ':') 
    c.setFont('Helvetica', 10)
    if academic.ScholarShip=='EX-SERVICE MAN QUOTA':
        ex='Yes'
    else:
        ex='N/A'
    c.drawString(230, 760, ex) 

    if academic.ScholarShip=='SPORTS QUOTA':
        sp='Yes'
    else:
        sp='N/A'

    if academic.ScholarShip=='DIFFERENTLY ABLED PERSON QUOTA':
        dfap='Yes'
    else:
        dfap='N/A'


    if academic.ScholarShip=='FIRST_GENERATION_GRADUATE':
        fg='Yes'
    else:
        fg='N/A'


    if academic.First_Graduate_certificate_No:
        fgc=academic.First_Graduate_certificate_No
    else:
        fgc='N/A'


    if academic.ScholarShip=='PMSS':
        pmss='Yes'
    else:
        pmss='N/A'

    if academic.ScholarShip=='GOVT_SCHOOL':
        gc='Yes'
    else:
        gc='N/A'

    if hsc.Twelfth_Std_Education_Qualified=='vocational':
        voc='Yes'
    else:
        voc='N/A'


    c.drawString(230, 730, sp) 
    c.drawString(230, 700, dfap) 
    c.drawString(230, 670, pmss) 
    c.drawString(230, 640, fg) 
    c.drawString(230, 610, fgc) 
    c.drawString(230, 580, gc) 
    c.drawString(230, 550, voc) 


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 520, 'VI. Occupation of Parent / Guardian')

    c.setFont('Helvetica', 10)
    c.rect(80, 460, 480, 30)
    c.rect(80, 430, 480, 30)
    c.line(190, 490, 190, 430) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 470, 'Occupation') 
    c.drawString(300, 470, 'Job Details') 
    c.setFont('Helvetica', 10)
    c.drawString(300, 440, academic.Occupation) 
    c.drawString(100, 440, academic.Job_Details) 

    c.drawString(30, 400, 'Family Annual Income of Parent / Guardian ') 
    c.drawString(30, 380, '(As per Income Certificate)') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 350, 'VII. a) Scholarship Information : (Only GQ)')

    c.setFont('Helvetica', 10)
    c.rect(80, 300, 480, 30)
    c.rect(80, 270, 480, 30)
    c.rect(80, 240, 480, 30)
    c.line(190, 330, 190, 240) 
    c.line(470, 330, 470, 240) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 310, 'Std') 
    c.drawString(300, 310, 'School Name') 
    c.drawString(490, 310, 'School Type') 
    c.setFont('Helvetica', 10)
    c.drawString(100, 280, '6th-10th') 
    c.drawString(300, 280, str(academic.Name_of_Std_6th_10th)) 
    c.drawString(490, 280, academic.Std_6th_10th_schooltype) 
    c.drawString(100, 250, '11th-12th') 
    c.drawString(300, 250, str(academic.School_Name_of_Std_11th_12th)) 
    c.drawString(490, 250, academic.Std_11th_12th_School_Type) 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 210, 'b) Student Bank Account Details :')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 180, 'Account Holder Name ') 
    c.drawString(30, 150, 'Name of the Bank ') 
    c.drawString(30, 120, 'Branch Name of the Bank') 
    c.drawString(30, 90, 'Branch Code Number') 
    c.drawString(30, 60, 'IFSC Code ') 
    c.drawString(30, 30, 'MICR Code ') 
    c.drawString(300, 180, 'Account Number ') 
    c.drawString(160, 180, ':') 
    c.drawString(160, 150, ':') 
    c.drawString(160, 120, ':') 
    c.drawString(160, 90, ':') 
    c.drawString(160, 60, ':') 
    c.drawString(160, 30, ':') 
    c.drawString(390, 180, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 180, academic.Bank_Holder_Name) 
    c.drawString(180, 150, academic.Name_of_the_Bank) 
    c.drawString(180, 120, academic.Branch_Name_of_the_Bank) 
    c.drawString(180, 90, academic.Branch_Code_No) 
    c.drawString(180, 60, academic.IFSC) 
    c.drawString(180, 30, academic.MICR) 
    c.drawString(400, 180, academic.Account_No) 

    c.showPage()
    c.drawCentredString(290, 820, ":: 5 ::")
    c.setFont('Helvetica-Bold', 14)
    c.drawString(30, 770, 'JOINT DECLARATION BY THE APPLICANT AND PARENT / GUARDIAN')
    c.setFont('Helvetica', 10)
    c.drawString(30, 750, 'We hereby solemnly affirm that the information furnished by us in the Application form and also in the enclosure there to')
    c.drawString(30, 730, 'submitted by us are true. If any information furnished therein is untrue in material particulars or on verification at a later')
    c.drawString(30, 710, 'stage, we are liable for criminal prosecution and we also agree to forgo the seat in this Institution / for removal')
    c.drawString(30, 690, "of student's name from roll of the Institution at whatever the stage of study he/she may be at the time of detection")
    c.drawString(30, 670, 'of such wrong particulars. If admitted, we agree to abide by the rules and regulations of the Institution and submit')
    c.drawString(30, 650, 'the Anti-ragging Affidavits by the Student and by the Parent within 2 weeks from the date of commencement')
    c.drawString(30, 630, 'of the Semester / College reopening. In the event of any violation of the College rules / Hostel rules by the Student')
    c.drawString(30, 610, 'we agree to obey the action taken by the Institution.')


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 510, 'Signature of the Parent / Guardian')
    c.drawString(330, 510, 'Signature of the Applicant')
    c.drawString(30, 450, 'Name')
    c.drawString(30, 410, 'Place')
    c.drawString(330, 450, 'Name')
    c.drawString(330, 410, 'Date of Admission ')

    c.drawString(70, 450, ':')
    c.drawString(70, 410, ':')
    c.drawString(420, 450, ':')
    c.drawString(420, 410, ':')
    c.setFont('Helvetica', 10)
    c.drawString(90, 450, personal_details.Father_name)
    c.drawString(90, 410, personal_details.Permanent_Address_Location)
    c.drawString(430, 450, personal_details.Name)
    c.drawString(430, 410, str(academic.dateadmission))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(230, 250, ' FOR OFFICE USE')
    c.drawString(150, 210, 'ADMISSION STATUS')
    c.drawString(150, 180, 'ADMITTED UNDER QUOTA')
    c.drawString(150, 150, 'BRANCH ALLOTTED ')
    c.drawString(280, 210, ':')
    c.drawString(285, 180, ':')
    c.drawString(280, 150, ':')
    c.setFont('Helvetica', 10)
    c.drawString(300, 210, 'ADMITTED')
    c.drawString(300, 180, personal_details.Quota)
    c.drawString(300, 150, personal_details.Department)




    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response





#.......................................Vocational pdf.....................................................................







def post_voc(request,admissionNo):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    hsc = HSC_Marks.objects.get(admissionNo=admissionNo)
    academic = Academic_Details.objects.get(admissionNo=admissionNo)

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

    
    c.setFont('Helvetica-Bold', 10)
    c.rect(465, 660, 90, 30)
    c.drawRightString(455, 675, "Application from ")
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.setFont('Helvetica', 10)
    c.drawString(470, 675, personal_details.admissionFor)  
    c.drawString(470, 635, personal_details.Quota)  # Replace with the actual quota
    c.drawString(470, 595, personal_details.Department)  # Replace with the actual branch
    c.drawString(470, 555, personal_details.Mode)  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)
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
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 485, 'Name') 
    c.drawString(155, 485, ':') 
    c.drawString(30, 455, 'Sex ') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Date Of Birth ') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Age') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Nationality') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Religion') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Mother Tounge') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nativity') 
    c.drawString(155, 275, ':') 

    c.drawString(30, 245, 'Self Mobile Number') 
    c.drawString(155, 245, ':') 

    c.drawString(30, 215, 'Self E - Mail ID') 
    c.drawString(155, 215, ':') 

    c.drawString(30, 185, 'Father Name') 
    c.drawString(155, 185, ':') 

    c.drawString(30, 155, 'Father Mobile Number') 
    c.drawString(155, 155, ':') 

    c.drawString(30, 125, 'Mother Name') 
    c.drawString(155, 125, ':') 

    c.drawString(30, 95, 'Mother Mobile Number') 
    c.drawString(155, 95, ':') 

    c.drawString(30, 65, 'Guardian Name') 
    c.drawString(155, 65, ':') 

    c.drawString(30, 35, 'Guardian Mobile Number') 
    c.drawString(155, 35, ':') 

    c.drawString(330, 485, 'Community') 
    c.drawString(400, 485, ':') 

    c.drawString(330, 455, 'Caste') 
    c.drawString(400, 455, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 485, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 335, personal_details.Religion) 
    c.drawString(180, 305, personal_details.Mother_Tongue) 
    c.drawString(180, 275, personal_details.Nativity) 
    c.drawString(180, 245, personal_details.Self_Mobile_Number) 
    c.drawString(180, 215, personal_details.Self_Mobile_Number) 
    c.drawString(180, 185, personal_details.Father_name) 
    c.drawString(180, 155, personal_details.Father_Mobile_Number) 
    c.drawString(180, 125, personal_details.Mother_name) 
    c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
    c.drawString(180, 65, personal_details.Guardian_name) 
    c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
    c.drawString(420, 485, personal_details.Community) 
    c.drawString(420, 455, personal_details.Caste) 




    c.showPage()
    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'II. Communication Details')

    # Draw the rectangle
    c.rect(100, 522, 480, 260)
    c.line(100, 742, 580, 742)  # Horizontal line under the permanent address
    c.line(100, 712, 580, 712)
    c.line(100, 682, 580, 682)
    c.line(100, 652, 580, 652)
    c.line(100, 622, 580, 622)
    c.line(100, 592, 580, 592)
    c.line(100, 562, 580, 562)
    c.line(330, 782, 330, 520)  #   vertical

    # Set the font
    c.setFont('Helvetica-Bold', 13)

    # Place the value inside the rectangle
    c.drawString(130, 755, 'Permanent Address')
    c.drawString(390, 755, 'Communication Address')
    c.setFont('Helvetica', 11)
    c.drawString(170, 725, personal_details.Permanent_Address_Door_No) 
    c.drawString(140, 695, personal_details.Permanent_Address_Street_Name) 
    c.drawString(150, 665, personal_details.Permanent_Address_Location) 
    c.drawString(165, 635, personal_details.Permanent_Address_Pincode) 
    c.drawString(150, 605, personal_details.Permanent_Address_Taluk) 
    c.drawString(150, 575, personal_details.Permanent_Address_District) 
    c.drawString(150, 545, personal_details.Permanent_Address_State) 

    c.drawString(450, 725, personal_details.Communication_Address_Door_No) 
    c.drawString(420, 695, personal_details.Communication_Address_Street_Name) 
    c.drawString(430, 665, personal_details.Communication_Address_Location) 
    c.drawString(445, 635, personal_details.Communication_Address_Pincode) 
    c.drawString(420, 605, personal_details.Communication_Address_Taluk) 
    c.drawString(420, 575, personal_details.Communication_Address_District) 
    c.drawString(420, 545, personal_details.Communication_Address_State) 

    c.drawString(30, 725, 'Door No') 
    c.drawString(30, 695, 'Street Name') 
    c.drawString(30, 665, 'Location ') 
    c.drawString(30, 635, 'Pincode') 
    c.drawString(30, 605, 'Taluk ') 
    c.drawString(30, 575, 'District ') 
    c.drawString(30, 545, 'State') 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 483, 'III. Admission Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 453, '1. Counselling Application Number :')
    c.drawString(350, 453, '2. Management Application Number :')
    c.drawString(30, 423, '3. Counselling General Rank  :')
    c.drawString(350, 423, '4. Counselling Community Rank :')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number :')

    c.setFont('Helvetica', 10)
    c.drawString(230, 453, str(academic.Counselling_Application_No))
    c.drawString(530, 453, 'academic')
    c.drawString(230, 423, str(academic.Counselling_General_Rank))
    c.drawString(530, 423, 'academic')
    c.drawString(230, 393, str(academic.GQ_admissionNo))
    
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 343, 'IV. Academic Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 313, 'a. EMIS Number')
    c.setFont('Helvetica', 10)
    c.drawString(120, 313, personal_details.EMIS_ID)
    c.rect(30, 263, 550, 30)
    c.rect(30, 203, 550, 60)
    c.rect(30, 120, 550, 30)
    c.rect(30, 60, 550, 60)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 277, '10th Std. School Information')
    c.drawString(35, 247, 'Name of the Institution :')
    c.drawString(435, 247, 'Year Of Passing :')
    c.drawString(35, 217, 'Place of the Institution :')
    c.drawString(235, 217, 'Board of Study :')
    c.drawString(435, 217, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 247, personal_details.Tenth_Std_School_Name)
    c.drawString(525, 247, str(personal_details.Tenth_Std_Year_of_Passing))
    c.drawString(150, 217, personal_details.Tenth_Std_Place_of_School)
    c.drawString(315, 217, personal_details.Tenth_Std_School_Type)
    c.drawString(525, 217, personal_details.Tenth_Std_Medium_of_Study)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 135, '11th Std. School Information')
    c.drawString(35, 103, 'Name of the Institution :')
    c.drawString(435, 103, 'Year Of Passing :')
    c.drawString(35, 71, 'Place of the Institution :')
    c.drawString(235, 71, 'Category :')
    c.drawString(435, 71, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 103, hsc.Eleventh_Std_School_Name)
    c.drawString(525, 103, str(hsc.Eleventh_Std_Year_of_Passing))
    c.drawString(150, 71, hsc.Eleventh_Std_Place_of_School)
    c.drawString(285, 71, hsc.Eleventh_Std_Category)
    c.drawString(525, 71, hsc.Eleventh_Std_Medium_of_Study)
    # Build the PDF document
    # Save the PDF
    c.showPage()
    c.drawCentredString(290, 820, ":: 3 ::")
    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, '12th Std. School Information')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, hsc.Twelfth_Std_School_Name)
    c.drawString(525, 745, str(hsc.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 715, hsc.Twelfth_Std_Place_of_School)
    c.drawString(285, 715, hsc.Twelfth_Std_Category)
    c.drawString(525, 715, hsc.Twelfth_Std_Medium_of_Study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.HSC Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'HSC Register Number :')
    c.drawString(50, 593, 'HSC Marksheet Number :')
    c.drawString(370, 623, 'HSC Studied In  :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, hsc.Twelfth_Std_Register_No)
    c.drawString(180, 593, hsc.Twelfth_Std_Marksheet_No)
    c.drawString(450, 623, hsc.Twelfth_Std_studied_in)


    c.rect(30, 543, 550, 30)
    c.rect(30, 363, 550, 180)
    c.line(290, 365, 290, 545) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 555, 'HSC Marks Scored in HSC Vocational ')
    c.drawString(70, 520, 'Language')
    c.drawString(70, 498, 'English')
    c.drawString(70, 473, 'Chemistry')
    c.drawString(70, 448, hsc.Twelfth_Std_voc_Mathematics_or_Physics_Name)
    c.drawString(70, 423, hsc.Twelfth_Std_voc_Vocational_Theory_Name)
    c.drawString(70, 398, 'Practical_Name')
    c.drawString(70, 373, 'Total')
    c.drawString(330, 398, 'Cutoff')
    c.drawString(330, 373, 'Percentage')
    c.drawString(140, 520, ':')
    c.drawString(140, 498, ':')
    c.drawString(140, 473, ':')
    c.drawString(140, 448, ':')
    c.drawString(140, 423, ':')
    c.drawString(140, 398, ':')
    c.drawString(140, 373, ':')
    c.drawString(390, 398, ':')
    c.drawString(390, 373, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 520, str(hsc.Twelfth_Std_voc_Language_Mark))
    c.drawString(150, 498, str(hsc.Twelfth_Std_voc_English_Mark))
    c.drawString(150, 473, str(hsc.Twelfth_Std_voc_chemistry_Mark))
    c.drawString(150, 448, str(hsc.Twelfth_Std_voc_Mathematics_or_Physics_Mark))
    c.drawString(150, 423, str(hsc.Twelfth_Std_voc_Vocational_Theory_Mark))
    c.drawString(150, 398, str(hsc.Twelfth_Std_voc_Practical_Mark))
    c.drawString(150, 373, str(hsc.Twelfth_Std_voc_Total_Marks))
    c.drawString(400, 398, str(hsc.Twelfth_Std_voc_CUT_OFF_Mark))
    c.drawString(400, 373, str(hsc.Twelfth_Std_voc_PCM_Average))
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 333, 'VI. SSLC Details')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 303, 'SSLC Register Number :')
    c.drawString(50, 273, 'SSLC Marksheet Number :')
    c.drawString(370, 303, 'SSLC Studied In :')
    c.drawString(370, 273, 'SSLC Exam Number :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 303, personal_details.Tenth_Std_Register_No)
    c.drawString(180, 273, personal_details.Tenth_Std_Marksheet_No)
    c.drawString(470, 303, personal_details.Tenth_Std_Studied_In)
    c.drawString(470, 273, personal_details.Tenth_Std_Roll_No)

    c.rect(30, 223, 550, 30)
    c.rect(30, 43, 550, 180)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 232, 'SSLC Marks Scored in HSC Vocational ')
    c.drawString(215, 207, 'Tamil')
    c.drawString(215, 182, 'English')
    c.drawString(215, 157, 'Mathematics')
    c.drawString(215, 132, 'Science')
    c.drawString(215, 107, 'Social Science ')
    c.drawString(215, 82, 'N/A ')
    c.drawString(215, 57, 'Total')
    c.drawString(300, 207, ':')
    c.drawString(300, 182, ':')
    c.drawString(300, 157, ':')
    c.drawString(300, 132, ':')
    c.drawString(300, 107, ': ')
    c.drawString(300, 82, ':')
    c.drawString(300, 57, ':')
    c.setFont('Helvetica', 10)
    c.drawString(320, 207, str(personal_details.Tenth_Std_Tamil_Mark))
    c.drawString(320, 182, str(personal_details.Tenth_Std_English_Mark))
    c.drawString(320, 157, str(personal_details.Tenth_Std_Maths_Mark))
    c.drawString(320, 132, str(personal_details.Tenth_Std_Science_Mark))
    c.drawString(320, 107, str(personal_details.Tenth_Std_SocialScience_Mark))
    c.drawString(320, 82, str(personal_details.Tenth_Std_Others_Mark))
    c.drawString(320, 57, str(personal_details.Tenth_Std_Obtain_Mark))
    c.showPage()
    c.drawCentredString(290, 820, ":: 4 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 790, 'V. Special Reservation Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 760, '1.Ex-Service Man Quota ') 
    c.drawString(30, 730, '2.Sports Quota ') 
    c.drawString(30, 700, '3.Differently abled Person Quota ') 
    c.drawString(30, 670, '4.PMSS (only SC/ST/SCA/SCC) ') 
    c.drawString(30, 640, '5.First Generation Graduate') 
    c.drawString(30, 610, '6.Certificate Number') 
    c.drawString(30, 580, "7.7.5% Govt. Quota") 
    c.drawString(30, 550, '8.Vocational') 

    c.drawString(200, 760, ':') 
    c.drawString(200, 730, ':') 
    c.drawString(200, 700, ':') 
    c.drawString(200, 670, ':') 
    c.drawString(200, 640, ':') 
    c.drawString(200, 610, ':') 
    c.drawString(200, 580, ':') 
    c.drawString(200, 550, ':') 

    c.setFont('Helvetica', 10)
    if academic.ScholarShip=='EX-SERVICE MAN QUOTA':
        ex='Yes'
    else:
        ex='N/A'
    c.drawString(230, 760, ex) 

    if academic.ScholarShip=='SPORTS QUOTA':
        sp='Yes'
    else:
        sp='N/A'

    if academic.ScholarShip=='DIFFERENTLY ABLED PERSON QUOTA':
        dfap='Yes'
    else:
        dfap='N/A'


    if academic.ScholarShip=='FIRST_GENERATION_GRADUATE':
        fg='Yes'
    else:
        fg='N/A'


    if academic.First_Graduate_certificate_No:
        fgc=academic.First_Graduate_certificate_No
    else:
        fgc='N/A'


    if academic.ScholarShip=='PMSS':
        pmss='Yes'
    else:
        pmss='N/A'

    if academic.ScholarShip=='GOVT_SCHOOL':
        gc='Yes'
    else:
        gc='N/A'

    if hsc.Twelfth_Std_Education_Qualified=='vocational':
        voc='Yes'
    else:
        voc='N/A'


    c.drawString(230, 730, sp) 
    c.drawString(230, 700, dfap) 
    c.drawString(230, 670, pmss) 
    c.drawString(230, 640, fg) 
    c.drawString(230, 610, fgc) 
    c.drawString(230, 580, gc) 
    c.drawString(230, 550, voc) 


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 520, 'VI. Occupation of Parent / Guardian')

    c.setFont('Helvetica', 10)
    c.rect(80, 460, 480, 30)
    c.rect(80, 430, 480, 30)
    c.line(190, 490, 190, 430) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 470, 'Occupation') 
    c.drawString(300, 470, 'Job Details') 
    c.setFont('Helvetica', 10)
    c.drawString(300, 440, academic.Occupation) 
    c.drawString(100, 440, academic.Job_Details) 

    c.drawString(30, 400, 'Family Annual Income of Parent / Guardian ') 
    c.drawString(30, 380, '(As per Income Certificate)') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 350, 'VII. a) Scholarship Information : (Only GQ)')

    c.setFont('Helvetica', 10)
    c.rect(80, 300, 480, 30)
    c.rect(80, 270, 480, 30)
    c.rect(80, 240, 480, 30)
    c.line(190, 330, 190, 240) 
    c.line(470, 330, 470, 240) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 310, 'Std') 
    c.drawString(300, 310, 'School Name') 
    c.drawString(490, 310, 'School Type') 
    c.setFont('Helvetica', 10)
    c.drawString(100, 280, '6th-10th') 
    c.drawString(300, 280, str(academic.Name_of_Std_6th_10th)) 
    c.drawString(490, 280, academic.Std_6th_10th_schooltype) 
    c.drawString(100, 250, '11th-12th') 
    c.drawString(300, 250, str(academic.School_Name_of_Std_11th_12th)) 
    c.drawString(490, 250, academic.Std_11th_12th_School_Type) 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 210, 'b) Student Bank Account Details :')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 180, 'Account Holder Name ') 
    c.drawString(30, 150, 'Name of the Bank ') 
    c.drawString(30, 120, 'Branch Name of the Bank') 
    c.drawString(30, 90, 'Branch Code Number') 
    c.drawString(30, 60, 'IFSC Code ') 
    c.drawString(30, 30, 'MICR Code ') 
    c.drawString(300, 180, 'Account Number ') 
    c.drawString(160, 180, ':') 
    c.drawString(160, 150, ':') 
    c.drawString(160, 120, ':') 
    c.drawString(160, 90, ':') 
    c.drawString(160, 60, ':') 
    c.drawString(160, 30, ':') 
    c.drawString(390, 180, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 180, academic.Bank_Holder_Name) 
    c.drawString(180, 150, academic.Name_of_the_Bank) 
    c.drawString(180, 120, academic.Branch_Name_of_the_Bank) 
    c.drawString(180, 90, academic.Branch_Code_No) 
    c.drawString(180, 60, academic.IFSC) 
    c.drawString(180, 30, academic.MICR) 
    c.drawString(400, 180, academic.Account_No) 

    c.showPage()
    c.drawCentredString(290, 820, ":: 5 ::")
    c.setFont('Helvetica-Bold', 14)
    c.drawString(30, 770, 'JOINT DECLARATION BY THE APPLICANT AND PARENT / GUARDIAN')
    c.setFont('Helvetica', 10)
    c.drawString(30, 750, 'We hereby solemnly affirm that the information furnished by us in the Application form and also in the enclosure there to')
    c.drawString(30, 730, 'submitted by us are true. If any information furnished therein is untrue in material particulars or on verification at a later')
    c.drawString(30, 710, 'stage, we are liable for criminal prosecution and we also agree to forgo the seat in this Institution / for removal')
    c.drawString(30, 690, "of student's name from roll of the Institution at whatever the stage of study he/she may be at the time of detection")
    c.drawString(30, 670, 'of such wrong particulars. If admitted, we agree to abide by the rules and regulations of the Institution and submit')
    c.drawString(30, 650, 'the Anti-ragging Affidavits by the Student and by the Parent within 2 weeks from the date of commencement')
    c.drawString(30, 630, 'of the Semester / College reopening. In the event of any violation of the College rules / Hostel rules by the Student')
    c.drawString(30, 610, 'we agree to obey the action taken by the Institution.')


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 510, 'Signature of the Parent / Guardian')
    c.drawString(330, 510, 'Signature of the Applicant')
    c.drawString(30, 450, 'Name')
    c.drawString(30, 410, 'Place')
    c.drawString(330, 450, 'Name')
    c.drawString(330, 410, 'Date of Admission ')

    c.drawString(70, 450, ':')
    c.drawString(70, 410, ':')
    c.drawString(420, 450, ':')
    c.drawString(420, 410, ':')
    c.setFont('Helvetica', 10)
    c.drawString(90, 450, personal_details.Father_name)
    c.drawString(90, 410, personal_details.Permanent_Address_Location)
    c.drawString(430, 450, personal_details.Name)
    c.drawString(430, 410, str(academic.dateadmission))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(230, 250, ' FOR OFFICE USE')
    c.drawString(150, 210, 'ADMISSION STATUS')
    c.drawString(150, 180, 'ADMITTED UNDER QUOTA')
    c.drawString(150, 150, 'BRANCH ALLOTTED ')
    c.drawString(280, 210, ':')
    c.drawString(285, 180, ':')
    c.drawString(280, 150, ':')
    c.setFont('Helvetica', 10)
    c.drawString(300, 210, 'ADMITTED')
    c.drawString(300, 180, personal_details.Quota)
    c.drawString(300, 150, personal_details.Department)




    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response




# /,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,post_dip..........................................................................









def post_dip(request,admissionNo):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    diplomo = Diplomo.objects.get(admissionNo=admissionNo)
    academic = Academic_Details.objects.get(admissionNo=admissionNo)
    hsc = HSC_Marks.objects.get(admissionNo=admissionNo)

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

    
    c.setFont('Helvetica-Bold', 10)
    c.rect(465, 660, 90, 30)
    c.drawRightString(455, 675, "Application from ")
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.setFont('Helvetica', 10)
    c.drawString(470, 675, personal_details.admissionFor)  
    c.drawString(470, 635, personal_details.Quota)  # Replace with the actual quota
    c.drawString(470, 595, personal_details.Department)  # Replace with the actual branch
    c.drawString(470, 555, personal_details.Mode)  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)
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
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 485, 'Name') 
    c.drawString(155, 485, ':') 
    c.drawString(30, 455, 'Sex ') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Date Of Birth ') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Age') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Nationality') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Religion') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Mother Tounge') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nativity') 
    c.drawString(155, 275, ':') 

    c.drawString(30, 245, 'Self Mobile Number') 
    c.drawString(155, 245, ':') 

    c.drawString(30, 215, 'Self E - Mail ID') 
    c.drawString(155, 215, ':') 

    c.drawString(30, 185, 'Father Name') 
    c.drawString(155, 185, ':') 

    c.drawString(30, 155, 'Father Mobile Number') 
    c.drawString(155, 155, ':') 

    c.drawString(30, 125, 'Mother Name') 
    c.drawString(155, 125, ':') 

    c.drawString(30, 95, 'Mother Mobile Number') 
    c.drawString(155, 95, ':') 

    c.drawString(30, 65, 'Guardian Name') 
    c.drawString(155, 65, ':') 

    c.drawString(30, 35, 'Guardian Mobile Number') 
    c.drawString(155, 35, ':') 

    c.drawString(330, 485, 'Community') 
    c.drawString(400, 485, ':') 

    c.drawString(330, 455, 'Caste') 
    c.drawString(400, 455, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 485, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 335, personal_details.Religion) 
    c.drawString(180, 305, personal_details.Mother_Tongue) 
    c.drawString(180, 275, personal_details.Nativity) 
    c.drawString(180, 245, personal_details.Self_Mobile_Number) 
    c.drawString(180, 215, personal_details.Self_Mobile_Number) 
    c.drawString(180, 185, personal_details.Father_name) 
    c.drawString(180, 155, personal_details.Father_Mobile_Number) 
    c.drawString(180, 125, personal_details.Mother_name) 
    c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
    c.drawString(180, 65, personal_details.Guardian_name) 
    c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
    c.drawString(420, 485, personal_details.Community) 
    c.drawString(420, 455, personal_details.Caste) 




    c.showPage()
    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'II. Communication Details')

    # Draw the rectangle
    c.rect(100, 522, 480, 260)
    c.line(100, 742, 580, 742)  # Horizontal line under the permanent address
    c.line(100, 712, 580, 712)
    c.line(100, 682, 580, 682)
    c.line(100, 652, 580, 652)
    c.line(100, 622, 580, 622)
    c.line(100, 592, 580, 592)
    c.line(100, 562, 580, 562)
    c.line(330, 782, 330, 520)  #   vertical

    # Set the font
    c.setFont('Helvetica-Bold', 13)

    # Place the value inside the rectangle
    c.drawString(130, 755, 'Permanent Address')
    c.drawString(390, 755, 'Communication Address')
    c.setFont('Helvetica', 11)
    c.drawString(170, 725, personal_details.Permanent_Address_Door_No) 
    c.drawString(140, 695, personal_details.Permanent_Address_Street_Name) 
    c.drawString(150, 665, personal_details.Permanent_Address_Location) 
    c.drawString(165, 635, personal_details.Permanent_Address_Pincode) 
    c.drawString(150, 605, personal_details.Permanent_Address_Taluk) 
    c.drawString(150, 575, personal_details.Permanent_Address_District) 
    c.drawString(150, 545, personal_details.Permanent_Address_State) 

    c.drawString(450, 725, personal_details.Communication_Address_Door_No) 
    c.drawString(420, 695, personal_details.Communication_Address_Street_Name) 
    c.drawString(430, 665, personal_details.Communication_Address_Location) 
    c.drawString(445, 635, personal_details.Communication_Address_Pincode) 
    c.drawString(420, 605, personal_details.Communication_Address_Taluk) 
    c.drawString(420, 575, personal_details.Communication_Address_District) 
    c.drawString(420, 545, personal_details.Communication_Address_State) 

    c.drawString(30, 725, 'Door No') 
    c.drawString(30, 695, 'Street Name') 
    c.drawString(30, 665, 'Location ') 
    c.drawString(30, 635, 'Pincode') 
    c.drawString(30, 605, 'Taluk ') 
    c.drawString(30, 575, 'District ') 
    c.drawString(30, 545, 'State') 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 483, 'III. Admission Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 453, '1. Counselling Application Number :')
    c.drawString(350, 453, '2. Management Application Number :')
    c.drawString(30, 423, '3. Counselling General Rank  :')
    c.drawString(350, 423, '4. Counselling Community Rank :')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number :')

    c.setFont('Helvetica', 10)
    c.drawString(230, 453, str(academic.Counselling_Application_No))
    c.drawString(530, 453, 'academic')
    c.drawString(230, 423, str(academic.Counselling_General_Rank))
    c.drawString(530, 423, 'academic')
    c.drawString(230, 393, str(academic.GQ_admissionNo))
    
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 343, 'IV. Academic Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 313, 'a. EMIS Number')
    c.setFont('Helvetica', 10)
    c.drawString(120, 313, personal_details.EMIS_ID)
    c.rect(30, 263, 550, 30)
    c.rect(30, 203, 550, 60)
  


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 277, '10th Std. School Information')
    c.drawString(35, 247, 'Name of the Institution :')
    c.drawString(435, 247, 'Year Of Passing :')
    c.drawString(35, 217, 'Place of the Institution :')
    c.drawString(235, 217, 'Board of Study :')
    c.drawString(435, 217, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 247, personal_details.Tenth_Std_School_Name)
    c.drawString(525, 247, str(personal_details.Tenth_Std_Year_of_Passing))
    c.drawString(150, 217, personal_details.Tenth_Std_Place_of_School)
    c.drawString(315, 217, personal_details.Tenth_Std_School_Type)
    c.drawString(525, 217, personal_details.Tenth_Std_Medium_of_Study)



    # Build the PDF document
    # Save the PDF
    c.showPage()
    c.drawCentredString(290, 820, ":: 3 ::")
    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, 'Name_of_the_Polytechnic_College')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, diplomo.Name_of_the_Polytechnic_College)
    c.drawString(525, 745, str(diplomo.year_of_passing))
    c.drawString(150, 715, diplomo.Polytechnic_College_place)
    c.drawString(285, 715, diplomo.Diploma_apply_for)
    c.drawString(525, 715, diplomo.medium_of_study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.Diploma Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'diplomo Register Number :')
    c.drawString(50, 593, 'diplomo diploma_certificate Number :')
    c.drawString(370, 623, 'diplomo Studied In  :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, diplomo.diploma_register_no)
    c.drawString(230, 593, diplomo.diploma_certificate_no)
    c.drawString(470, 623, diplomo.diploma_studied_in)


    c.rect(30, 543, 550, 30)
    c.rect(30, 363, 550, 180)
    c.line(290, 365, 290, 545) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 555, 'Diploma Marks Scored in Diploma ')
    c.drawString(70, 520, 'Sem1')
    c.drawString(70, 498, 'Sem2')
    c.drawString(70, 473, 'Sem3')
    c.drawString(70, 448, 'Sem4')
    c.drawString(70, 423, 'Sem5')
    c.drawString(70, 398, 'Sem6')
    c.drawString(70, 373, 'Total')
    c.drawString(330, 398, 'obtain_mark')
    c.drawString(330, 373, 'percentages')
    c.drawString(140, 520, ':')
    c.drawString(140, 498, ':')
    c.drawString(140, 473, ':')
    c.drawString(140, 448, ':')
    c.drawString(140, 423, ':')
    c.drawString(140, 398, ':')
    c.drawString(140, 373, ':')
    c.drawString(390, 398, ':')
    c.drawString(390, 373, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 520, str(diplomo.sem1_obtain_mark))
    c.drawString(150, 498, str(diplomo.sem2_obtain_mark))
    c.drawString(150, 473, str(diplomo.sem3_obtain_mark))
    c.drawString(150, 448, str(diplomo.sem4_obtain_mark))
    c.drawString(150, 423, str(diplomo.sem5_obtain_mark))
    c.drawString(150, 398, str(diplomo.sem6_obtain_mark))
    c.drawString(150, 373, str(diplomo.diploma_total_mark))
    c.drawString(400, 398, str(diplomo.diploma_obtain_mark))
    c.drawString(400, 373, str(diplomo.total_percentages))
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 333, 'VI. SSLC Details')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 303, 'SSLC Register Number :')
    c.drawString(50, 273, 'SSLC Marksheet Number :')
    c.drawString(370, 303, 'SSLC Studied In :')
    c.drawString(370, 273, 'SSLC Exam Number :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 303, personal_details.Tenth_Std_Register_No)
    c.drawString(180, 273, personal_details.Tenth_Std_Marksheet_No)
    c.drawString(470, 303, personal_details.Tenth_Std_Studied_In)
    c.drawString(470, 273, personal_details.Tenth_Std_Roll_No)

    c.rect(30, 223, 550, 30)
    c.rect(30, 43, 550, 180)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 232, 'SSLC Marks Scored in Diploma')
    c.drawString(215, 207, 'Tamil')
    c.drawString(215, 182, 'English')
    c.drawString(215, 157, 'Mathematics')
    c.drawString(215, 132, 'Science')
    c.drawString(215, 107, 'Social Science ')
    c.drawString(215, 82, 'N/A ')
    c.drawString(215, 57, 'Total')
    c.drawString(300, 207, ':')
    c.drawString(300, 182, ':')
    c.drawString(300, 157, ':')
    c.drawString(300, 132, ':')
    c.drawString(300, 107, ': ')
    c.drawString(300, 82, ':')
    c.drawString(300, 57, ':')
    c.setFont('Helvetica', 10)
    c.drawString(320, 207, str(personal_details.Tenth_Std_Tamil_Mark))
    c.drawString(320, 182, str(personal_details.Tenth_Std_English_Mark))
    c.drawString(320, 157, str(personal_details.Tenth_Std_Maths_Mark))
    c.drawString(320, 132, str(personal_details.Tenth_Std_Science_Mark))
    c.drawString(320, 107, str(personal_details.Tenth_Std_SocialScience_Mark))
    c.drawString(320, 82, str(personal_details.Tenth_Std_Others_Mark))
    c.drawString(320, 57, str(personal_details.Tenth_Std_Obtain_Mark))
    c.showPage()
    c.drawCentredString(290, 820, ":: 4 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 790, 'V. Special Reservation Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 760, '1.Ex-Service Man Quota ') 
    c.drawString(30, 730, '2.Sports Quota ') 
    c.drawString(30, 700, '3.Differently abled Person Quota ') 
    c.drawString(30, 670, '4.PMSS (only SC/ST/SCA/SCC) ') 
    c.drawString(30, 640, '5.First Generation Graduate') 
    c.drawString(30, 610, '6.Certificate Number') 
    c.drawString(30, 580, "7.7.5% Govt. Quota") 
    c.drawString(30, 550, '8.Vocational') 

    c.drawString(200, 760, ':') 
    c.drawString(200, 730, ':') 
    c.drawString(200, 700, ':') 
    c.drawString(200, 670, ':') 
    c.drawString(200, 640, ':') 
    c.drawString(200, 610, ':') 
    c.drawString(200, 580, ':') 
    c.drawString(200, 550, ':') 
    c.setFont('Helvetica', 10)
    if academic.ScholarShip=='EX-SERVICE MAN QUOTA':
        ex='Yes'
    else:
        ex='N/A'
    c.drawString(230, 760, ex) 

    if academic.ScholarShip=='SPORTS QUOTA':
        sp='Yes'
    else:
        sp='N/A'

    if academic.ScholarShip=='DIFFERENTLY ABLED PERSON QUOTA':
        dfap='Yes'
    else:
        dfap='N/A'


    if academic.ScholarShip=='FIRST_GENERATION_GRADUATE':
        fg='Yes'
    else:
        fg='N/A'


    if academic.First_Graduate_certificate_No:
        fgc=academic.First_Graduate_certificate_No
    else:
        fgc='N/A'


    if academic.ScholarShip=='PMSS':
        pmss='Yes'
    else:
        pmss='N/A'

    if academic.ScholarShip=='GOVT_SCHOOL':
        gc='Yes'
    else:
        gc='N/A'

    if hsc.Twelfth_Std_Education_Qualified=='vocational':
        voc='Yes'
    else:
        voc='N/A'


    c.drawString(230, 730, sp) 
    c.drawString(230, 700, dfap) 
    c.drawString(230, 670, pmss) 
    c.drawString(230, 640, fg) 
    c.drawString(230, 610, fgc) 
    c.drawString(230, 580, gc) 
    c.drawString(230, 550, voc) 


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 520, 'VI. Occupation of Parent / Guardian')

    c.setFont('Helvetica', 10)
    c.rect(80, 460, 480, 30)
    c.rect(80, 430, 480, 30)
    c.line(190, 490, 190, 430) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 470, 'Occupation') 
    c.drawString(300, 470, 'Job Details') 
    c.setFont('Helvetica', 10)
    c.drawString(300, 440, academic.Occupation) 
    c.drawString(100, 440, academic.Job_Details) 

    c.drawString(30, 400, 'Family Annual Income of Parent / Guardian ') 
    c.drawString(30, 380, '(As per Income Certificate)') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 350, 'VII. a) Scholarship Information : (Only GQ)')

    c.setFont('Helvetica', 10)
    c.rect(80, 300, 480, 30)
    c.rect(80, 270, 480, 30)
    c.rect(80, 240, 480, 30)
    c.line(190, 330, 190, 240) 
    c.line(470, 330, 470, 240) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 310, 'Std') 
    c.drawString(300, 310, 'School Name') 
    c.drawString(490, 310, 'School Type') 
    c.setFont('Helvetica', 10)
    c.drawString(100, 280, '6th-10th') 
    c.drawString(300, 280, str(academic.Name_of_Std_6th_10th)) 
    c.drawString(490, 280, academic.Std_6th_10th_schooltype) 
    c.drawString(100, 250, '11th-12th') 
    c.drawString(300, 250, str(academic.School_Name_of_Std_11th_12th)) 
    c.drawString(490, 250, academic.Std_11th_12th_School_Type) 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 210, 'b) Student Bank Account Details :')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 180, 'Account Holder Name ') 
    c.drawString(30, 150, 'Name of the Bank ') 
    c.drawString(30, 120, 'Branch Name of the Bank') 
    c.drawString(30, 90, 'Branch Code Number') 
    c.drawString(30, 60, 'IFSC Code ') 
    c.drawString(30, 30, 'MICR Code ') 
    c.drawString(300, 180, 'Account Number ') 
    c.drawString(160, 180, ':') 
    c.drawString(160, 150, ':') 
    c.drawString(160, 120, ':') 
    c.drawString(160, 90, ':') 
    c.drawString(160, 60, ':') 
    c.drawString(160, 30, ':') 
    c.drawString(390, 180, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 180, academic.Bank_Holder_Name) 
    c.drawString(180, 150, academic.Name_of_the_Bank) 
    c.drawString(180, 120, academic.Branch_Name_of_the_Bank) 
    c.drawString(180, 90, academic.Branch_Code_No) 
    c.drawString(180, 60, academic.IFSC) 
    c.drawString(180, 30, academic.MICR) 
    c.drawString(400, 180, academic.Account_No) 

    c.showPage()
    c.drawCentredString(290, 820, ":: 5 ::")
    c.setFont('Helvetica-Bold', 14)
    c.drawString(30, 770, 'JOINT DECLARATION BY THE APPLICANT AND PARENT / GUARDIAN')
    c.setFont('Helvetica', 10)
    c.drawString(30, 750, 'We hereby solemnly affirm that the information furnished by us in the Application form and also in the enclosure there to')
    c.drawString(30, 730, 'submitted by us are true. If any information furnished therein is untrue in material particulars or on verification at a later')
    c.drawString(30, 710, 'stage, we are liable for criminal prosecution and we also agree to forgo the seat in this Institution / for removal')
    c.drawString(30, 690, "of student's name from roll of the Institution at whatever the stage of study he/she may be at the time of detection")
    c.drawString(30, 670, 'of such wrong particulars. If admitted, we agree to abide by the rules and regulations of the Institution and submit')
    c.drawString(30, 650, 'the Anti-ragging Affidavits by the Student and by the Parent within 2 weeks from the date of commencement')
    c.drawString(30, 630, 'of the Semester / College reopening. In the event of any violation of the College rules / Hostel rules by the Student')
    c.drawString(30, 610, 'we agree to obey the action taken by the Institution.')


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 510, 'Signature of the Parent / Guardian')
    c.drawString(330, 510, 'Signature of the Applicant')
    c.drawString(30, 450, 'Name')
    c.drawString(30, 410, 'Place')
    c.drawString(330, 450, 'Name')
    c.drawString(330, 410, 'Date of Admission ')

    c.drawString(70, 450, ':')
    c.drawString(70, 410, ':')
    c.drawString(420, 450, ':')
    c.drawString(420, 410, ':')
    c.setFont('Helvetica', 10)
    c.drawString(90, 450, personal_details.Father_name)
    c.drawString(90, 410, personal_details.Permanent_Address_Location)
    c.drawString(430, 450, personal_details.Name)
    c.drawString(430, 410, str(academic.dateadmission))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(230, 250, ' FOR OFFICE USE')
    c.drawString(150, 210, 'ADMISSION STATUS')
    c.drawString(150, 180, 'ADMITTED UNDER QUOTA')
    c.drawString(150, 150, 'BRANCH ALLOTTED ')
    c.drawString(280, 210, ':')
    c.drawString(285, 180, ':')
    c.drawString(280, 150, ':')
    c.setFont('Helvetica', 10)
    c.drawString(300, 210, 'ADMITTED')
    c.drawString(300, 180, personal_details.Quota)
    c.drawString(300, 150, personal_details.Department)




    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response




# ....................................................post_dip_aca....................................................................








def post_dip_aca(request,admissionNo):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    hsc = HSC_Marks.objects.get(admissionNo=admissionNo)
    academic = Academic_Details.objects.get(admissionNo=admissionNo)
    diplomo = Diplomo.objects.get(admissionNo=admissionNo)

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

    
    c.setFont('Helvetica-Bold', 10)
    c.rect(465, 660, 90, 30)
    c.drawRightString(455, 675, "Application from ")
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.setFont('Helvetica', 10)
    c.drawString(470, 675, personal_details.admissionFor)  
    c.drawString(470, 635, personal_details.Quota)  # Replace with the actual quota
    c.drawString(470, 595, personal_details.Department)  # Replace with the actual branch
    c.drawString(470, 555, personal_details.Mode)  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)
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
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 485, 'Name') 
    c.drawString(155, 485, ':') 
    c.drawString(30, 455, 'Sex ') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Date Of Birth ') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Age') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Nationality') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Religion') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Mother Tounge') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nativity') 
    c.drawString(155, 275, ':') 

    c.drawString(30, 245, 'Self Mobile Number') 
    c.drawString(155, 245, ':') 

    c.drawString(30, 215, 'Self E - Mail ID') 
    c.drawString(155, 215, ':') 

    c.drawString(30, 185, 'Father Name') 
    c.drawString(155, 185, ':') 

    c.drawString(30, 155, 'Father Mobile Number') 
    c.drawString(155, 155, ':') 

    c.drawString(30, 125, 'Mother Name') 
    c.drawString(155, 125, ':') 

    c.drawString(30, 95, 'Mother Mobile Number') 
    c.drawString(155, 95, ':') 

    c.drawString(30, 65, 'Guardian Name') 
    c.drawString(155, 65, ':') 

    c.drawString(30, 35, 'Guardian Mobile Number') 
    c.drawString(155, 35, ':') 

    c.drawString(330, 485, 'Community') 
    c.drawString(400, 485, ':') 

    c.drawString(330, 455, 'Caste') 
    c.drawString(400, 455, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 485, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 335, personal_details.Religion) 
    c.drawString(180, 305, personal_details.Mother_Tongue) 
    c.drawString(180, 275, personal_details.Nativity) 
    c.drawString(180, 245, personal_details.Self_Mobile_Number) 
    c.drawString(180, 215, personal_details.Self_Mobile_Number) 
    c.drawString(180, 185, personal_details.Father_name) 
    c.drawString(180, 155, personal_details.Father_Mobile_Number) 
    c.drawString(180, 125, personal_details.Mother_name) 
    c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
    c.drawString(180, 65, personal_details.Guardian_name) 
    c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
    c.drawString(420, 485, personal_details.Community) 
    c.drawString(420, 455, personal_details.Caste) 




    c.showPage()
    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'II. Communication Details')

    # Draw the rectangle
    c.rect(100, 522, 480, 260)
    c.line(100, 742, 580, 742)  # Horizontal line under the permanent address
    c.line(100, 712, 580, 712)
    c.line(100, 682, 580, 682)
    c.line(100, 652, 580, 652)
    c.line(100, 622, 580, 622)
    c.line(100, 592, 580, 592)
    c.line(100, 562, 580, 562)
    c.line(330, 782, 330, 520)  #   vertical

    # Set the font
    c.setFont('Helvetica-Bold', 13)

    # Place the value inside the rectangle
    c.drawString(130, 755, 'Permanent Address')
    c.drawString(390, 755, 'Communication Address')
    c.setFont('Helvetica', 11)
    c.drawString(170, 725, personal_details.Permanent_Address_Door_No) 
    c.drawString(140, 695, personal_details.Permanent_Address_Street_Name) 
    c.drawString(150, 665, personal_details.Permanent_Address_Location) 
    c.drawString(165, 635, personal_details.Permanent_Address_Pincode) 
    c.drawString(150, 605, personal_details.Permanent_Address_Taluk) 
    c.drawString(150, 575, personal_details.Permanent_Address_District) 
    c.drawString(150, 545, personal_details.Permanent_Address_State) 

    c.drawString(450, 725, personal_details.Communication_Address_Door_No) 
    c.drawString(420, 695, personal_details.Communication_Address_Street_Name) 
    c.drawString(430, 665, personal_details.Communication_Address_Location) 
    c.drawString(445, 635, personal_details.Communication_Address_Pincode) 
    c.drawString(420, 605, personal_details.Communication_Address_Taluk) 
    c.drawString(420, 575, personal_details.Communication_Address_District) 
    c.drawString(420, 545, personal_details.Communication_Address_State) 

    c.drawString(30, 725, 'Door No') 
    c.drawString(30, 695, 'Street Name') 
    c.drawString(30, 665, 'Location ') 
    c.drawString(30, 635, 'Pincode') 
    c.drawString(30, 605, 'Taluk ') 
    c.drawString(30, 575, 'District ') 
    c.drawString(30, 545, 'State') 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 483, 'III. Admission Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 453, '1. Counselling Application Number :')
    c.drawString(350, 453, '2. Management Application Number :')
    c.drawString(30, 423, '3. Counselling General Rank  :')
    c.drawString(350, 423, '4. Counselling Community Rank :')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number :')

    c.setFont('Helvetica', 10)
    c.drawString(230, 453, str(academic.Counselling_Application_No))
    c.drawString(530, 453, 'academic')
    c.drawString(230, 423, str(academic.Counselling_General_Rank))
    c.drawString(530, 423, 'academic')
    c.drawString(230, 393, str(academic.GQ_admissionNo))
    
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 343, 'IV. Academic Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 313, 'a. EMIS Number')
    c.setFont('Helvetica', 10)
    c.drawString(120, 313, personal_details.EMIS_ID)
    c.rect(30, 263, 550, 30)
    c.rect(30, 203, 550, 60)
    c.rect(30, 120, 550, 30)
    c.rect(30, 60, 550, 60)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 277, '10th Std. School Information')
    c.drawString(35, 247, 'Name of the Institution :')
    c.drawString(435, 247, 'Year Of Passing :')
    c.drawString(35, 217, 'Place of the Institution :')
    c.drawString(235, 217, 'Board of Study :')
    c.drawString(435, 217, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 247, personal_details.Tenth_Std_School_Name)
    c.drawString(525, 247, str(personal_details.Tenth_Std_Year_of_Passing))
    c.drawString(150, 217, personal_details.Tenth_Std_Place_of_School)
    c.drawString(315, 217, personal_details.Tenth_Std_School_Type)
    c.drawString(525, 217, personal_details.Tenth_Std_Medium_of_Study)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 135, '11th Std. School Information')
    c.drawString(35, 103, 'Name of the Institution :')
    c.drawString(435, 103, 'Year Of Passing :')
    c.drawString(35, 71, 'Place of the Institution :')
    c.drawString(235, 71, 'Category :')
    c.drawString(435, 71, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 103, hsc.Eleventh_Std_School_Name)
    c.drawString(525, 103, str(hsc.Eleventh_Std_Year_of_Passing))
    c.drawString(150, 71, hsc.Eleventh_Std_Place_of_School)
    c.drawString(285, 71, hsc.Eleventh_Std_Category)
    c.drawString(525, 71, hsc.Eleventh_Std_Medium_of_Study)
    # Build the PDF document
    # Save the PDF
    c.showPage()
    c.drawCentredString(290, 820, ":: 3 ::")
    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, '12th Std. School Information')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, hsc.Twelfth_Std_School_Name)
    c.drawString(525, 745, str(hsc.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 715, hsc.Twelfth_Std_Place_of_School)
    c.drawString(285, 715, hsc.Twelfth_Std_Category)
    c.drawString(525, 715, hsc.Twelfth_Std_Medium_of_Study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.HSC Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'HSC Register Number :')
    c.drawString(50, 593, 'HSC Marksheet Number :')
    c.drawString(370, 623, 'HSC Studied In  :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, hsc.Twelfth_Std_Register_No)
    c.drawString(180, 593, hsc.Twelfth_Std_Marksheet_No)
    c.drawString(450, 623, hsc.Twelfth_Std_studied_in)


    c.rect(30, 543, 550, 30)
    c.rect(30, 363, 550, 180)
    c.line(290, 365, 290, 545) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 555, 'HSC Marks Scored in HSC Academic ')
    c.drawString(70, 520, 'Language')
    c.drawString(70, 498, 'English')
    c.drawString(70, 473, 'Mathematics')
    c.drawString(70, 448, 'Physics')
    c.drawString(70, 423, 'Chemistry')
    c.drawString(70, 398, 'Biology')
    c.drawString(70, 373, 'Total')
    c.drawString(330, 398, 'Cutoff')
    c.drawString(330, 373, 'Percentage')
    c.drawString(140, 520, ':')
    c.drawString(140, 498, ':')
    c.drawString(140, 473, ':')
    c.drawString(140, 448, ':')
    c.drawString(140, 423, ':')
    c.drawString(140, 398, ':')
    c.drawString(140, 373, ':')
    c.drawString(390, 398, ':')
    c.drawString(390, 373, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 520, str(hsc.Twelfth_Std_aca_Language_Mark))
    c.drawString(150, 498, str(hsc.Twelfth_Std_aca_English_Mark))
    c.drawString(150, 473, str(hsc.Twelfth_Std_aca_Mathematics_Mark))
    c.drawString(150, 448, str(hsc.Twelfth_Std_aca_Physics_Mark))
    c.drawString(150, 423, str(hsc.Twelfth_Std_aca_Chemistry_Mark))
    c.drawString(150, 398, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(150, 373, str(hsc.Twelfth_Std_aca_Total_Marks))
    c.drawString(400, 398, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(400, 373, str(hsc.Twelfth_Std_aca_Total_Marks))
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 333, 'VI. SSLC Details')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 303, 'SSLC Register Number :')
    c.drawString(50, 273, 'SSLC Marksheet Number :')
    c.drawString(370, 303, 'SSLC Studied In :')
    c.drawString(370, 273, 'SSLC Exam Number :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 303, personal_details.Tenth_Std_Register_No)
    c.drawString(180, 273, personal_details.Tenth_Std_Marksheet_No)
    c.drawString(470, 303, personal_details.Tenth_Std_Studied_In)
    c.drawString(470, 273, personal_details.Tenth_Std_Roll_No)

    c.rect(30, 223, 550, 30)
    c.rect(30, 43, 550, 180)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 232, 'SSLC Marks Scored in HSC Academic ')
    c.drawString(215, 207, 'Tamil')
    c.drawString(215, 182, 'English')
    c.drawString(215, 157, 'Mathematics')
    c.drawString(215, 132, 'Science')
    c.drawString(215, 107, 'Social Science ')
    c.drawString(215, 82, 'N/A ')
    c.drawString(215, 57, 'Total')
    c.drawString(300, 207, ':')
    c.drawString(300, 182, ':')
    c.drawString(300, 157, ':')
    c.drawString(300, 132, ':')
    c.drawString(300, 107, ': ')
    c.drawString(300, 82, ':')
    c.drawString(300, 57, ':')
    c.setFont('Helvetica', 10)
    c.drawString(320, 207, str(personal_details.Tenth_Std_Tamil_Mark))
    c.drawString(320, 182, str(personal_details.Tenth_Std_English_Mark))
    c.drawString(320, 157, str(personal_details.Tenth_Std_Maths_Mark))
    c.drawString(320, 132, str(personal_details.Tenth_Std_Science_Mark))
    c.drawString(320, 107, str(personal_details.Tenth_Std_SocialScience_Mark))
    c.drawString(320, 82, str(personal_details.Tenth_Std_Others_Mark))
    c.drawString(320, 57, str(personal_details.Tenth_Std_Obtain_Mark))
    c.showPage()

    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, 'Name_of_the_Polytechnic_College')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, diplomo.Name_of_the_Polytechnic_College)
    c.drawString(525, 745, str(diplomo.year_of_passing))
    c.drawString(150, 715, diplomo.Polytechnic_College_place)
    c.drawString(285, 715, diplomo.Diploma_apply_for)
    c.drawString(525, 715, diplomo.medium_of_study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.Diploma Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'diplomo Register Number :')
    c.drawString(420, 623, 'dip certificate No :')
    c.drawString(260, 623, 'diplomo Studied In  :')

    c.drawString(50, 593, 'dip total_percentages:')
    c.drawString(420, 593, 'dip total_mark:')
    c.drawString(260, 593, 'dip obtain_mark :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, diplomo.diploma_register_no)
    c.drawString(510, 623, diplomo.diploma_certificate_no)
    c.drawString(370, 623, diplomo.diploma_studied_in)

    c.drawString(180, 593, diplomo.total_percentages)
    c.drawString(510, 593, diplomo.diploma_total_mark)
    c.drawString(370, 593, diplomo.diploma_obtain_mark)

    c.setFont('Helvetica-Bold', 13)
    c.line(150, 530, 150, 470)
    c.line(300, 530, 300, 470) 
    c.line(450, 530, 450, 470) 
 
    c.rect(30, 530, 550, 30)
    c.rect(30, 500, 550, 30)
    c.rect(30, 470, 550, 30)

    c.setFont('Helvetica-Bold', 10)

    c.drawString(215, 540, 'Diploma Marks Scored in Diploma ')

    c.drawString(70, 513, 'Sem3')
    c.drawString(210, 513, 'Sem4')
    c.drawString(360, 513, 'Sem5')
    c.drawString(500, 513, 'Sem6')

    c.setFont('Helvetica', 10)
    c.drawString(70, 483, diplomo.sem3_obtain_mark)
    c.drawString(210, 483, diplomo.sem4_obtain_mark)
    c.drawString(360, 483, diplomo.sem5_obtain_mark)
    c.drawString(500, 483, diplomo.sem6_obtain_mark)

    c.drawCentredString(290, 820, ":: 4 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 440, 'V. Special Reservation Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(330, 410, '5.Ex-Service Man Quota ') 
    c.drawString(330, 380, '6.Sports Quota ') 
    c.drawString(330, 350, '7.Differently abled Person Quota ') 
    c.drawString(330, 320, '8.PMSS (only SC/ST/SCA/SCC) ') 
    c.drawString(30, 410, '1.First Generation Graduate') 
    c.drawString(30, 380, '2.Certificate Number') 
    c.drawString(30, 350, "3.7.5% Govt. Quota") 
    c.drawString(30, 320, '4.Vocational') 

    c.drawString(500, 410, ':') 
    c.drawString(500, 380, ':') 
    c.drawString(500, 350, ':') 
    c.drawString(500, 320, ':') 
    c.drawString(200, 410, ':') 
    c.drawString(200, 380, ':') 
    c.drawString(200, 350, ':') 
    c.drawString(200, 320, ':') 
    c.setFont('Helvetica', 10)
    if academic.ScholarShip=='EX-SERVICE MAN QUOTA':
        ex='Yes'
    else:
        ex='N/A'
    c.drawString(230, 410, ex) 

    if academic.ScholarShip=='SPORTS QUOTA':
        sp='Yes'
    else:
        sp='N/A'

    if academic.ScholarShip=='DIFFERENTLY ABLED PERSON QUOTA':
        dfap='Yes'
    else:
        dfap='N/A'


    if academic.ScholarShip=='FIRST_GENERATION_GRADUATE':
        fg='Yes'
    else:
        fg='N/A'


    if academic.First_Graduate_certificate_No:
        fgc=academic.First_Graduate_certificate_No
    else:
        fgc='N/A'


    if academic.ScholarShip=='PMSS':
        pmss='Yes'
    else:
        pmss='N/A'

    if academic.ScholarShip=='GOVT_SCHOOL':
        gc='Yes'
    else:
        gc='N/A'

    if hsc.Twelfth_Std_Education_Qualified=='vocational':
        voc='Yes'
    else:
        voc='N/A'


    c.drawString(530, 380, sp) 
    c.drawString(530, 350, dfap) 
    c.drawString(530, 320, pmss) 
    c.drawString(530, 410, fg) 
    c.drawString(230, 380, fgc) 
    c.drawString(230, 350, gc) 
    c.drawString(230, 320, voc) 


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 290, 'VI. Occupation of Parent / Guardian')

    c.setFont('Helvetica', 10)
    c.rect(80, 240, 480, 30)
    c.rect(80, 210, 480, 30)
    c.line(190, 270, 190, 210) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 250, 'Occupation') 
    c.drawString(300, 220, 'Job Details') 
    c.setFont('Helvetica', 10)
    c.drawString(300, 250, academic.Occupation) 
    c.drawString(100, 220, academic.Job_Details) 

    c.drawString(30, 180, 'Family Annual Income of Parent / Guardian ') 
    c.drawString(30, 150, '(As per Income Certificate)') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 130, 'VII. a) Scholarship Information : (Only GQ)')

    c.setFont('Helvetica', 10)
    c.rect(80, 80, 480, 30)
    c.rect(80, 50, 480, 30)
    c.rect(80, 20, 480, 30)
    c.line(190, 110, 190, 20) 
    c.line(470, 110, 470, 20) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 90, 'Std') 
    c.drawString(300, 90, 'School Name') 
    c.drawString(490, 90, 'School Type') 
    c.setFont('Helvetica', 10)
    c.drawString(100, 60, '6th-10th') 
    c.drawString(300, 60, str(academic.Name_of_Std_6th_10th)) 
    c.drawString(490, 60, academic.Std_6th_10th_schooltype) 
    c.drawString(100, 30, '11th-12th') 
    c.drawString(300, 30, str(academic.School_Name_of_Std_11th_12th)) 
    c.drawString(490, 30, academic.Std_11th_12th_School_Type) 



    c.showPage()
    c.drawCentredString(290, 820, ":: 5 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'b) Student Bank Account Details :')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 770, 'Account Holder Name ') 
    c.drawString(30, 740, 'Name of the Bank ') 
    c.drawString(30, 710, 'Branch Name of the Bank') 
    c.drawString(30, 680, 'Branch Code Number') 
    c.drawString(30, 650, 'IFSC Code ') 
    c.drawString(30, 620, 'MICR Code ') 
    c.drawString(300, 770, 'Account Number ') 
    c.drawString(160, 770, ':') 
    c.drawString(160, 740, ':') 
    c.drawString(160, 710, ':') 
    c.drawString(160, 680, ':') 
    c.drawString(160, 650, ':') 
    c.drawString(160, 620, ':') 
    c.drawString(390, 770, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 770, academic.Bank_Holder_Name) 
    c.drawString(180, 740, academic.Name_of_the_Bank) 
    c.drawString(180, 710, academic.Branch_Name_of_the_Bank) 
    c.drawString(180, 680, academic.Branch_Code_No) 
    c.drawString(180, 650, academic.IFSC) 
    c.drawString(180, 620, academic.MICR) 
    c.drawString(400, 770, academic.Account_No) 
    c.setFont('Helvetica-Bold', 14)
    c.drawString(30, 590, 'JOINT DECLARATION BY THE APPLICANT AND PARENT / GUARDIAN')
    c.setFont('Helvetica', 10)
    c.drawString(30, 560, 'We hereby solemnly affirm that the information furnished by us in the Application form and also in the enclosure there to')
    c.drawString(30, 540, 'submitted by us are true. If any information furnished therein is untrue in material particulars or on verification at a later')
    c.drawString(30, 520, 'stage, we are liable for criminal prosecution and we also agree to forgo the seat in this Institution / for removal')
    c.drawString(30, 500, "of student's name from roll of the Institution at whatever the stage of study he/she may be at the time of detection")
    c.drawString(30, 480, 'of such wrong particulars. If admitted, we agree to abide by the rules and regulations of the Institution and submit')
    c.drawString(30, 460, 'the Anti-ragging Affidavits by the Student and by the Parent within 2 weeks from the date of commencement')
    c.drawString(30, 440, 'of the Semester / College reopening. In the event of any violation of the College rules / Hostel rules by the Student')
    c.drawString(30, 420, 'we agree to obey the action taken by the Institution.')


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 350, 'Signature of the Parent / Guardian')
    c.drawString(330, 350, 'Signature of the Applicant')
    c.drawString(30, 280, 'Name')
    c.drawString(30, 230, 'Place')
    c.drawString(330, 280, 'Name')
    c.drawString(330, 230, 'Date of Admission ')

    c.drawString(70, 280, ':')
    c.drawString(70, 230, ':')
    c.drawString(420, 280, ':')
    c.drawString(420, 230, ':')
    c.setFont('Helvetica', 10)
    c.drawString(90, 280, personal_details.Father_name)
    c.drawString(90, 230, personal_details.Permanent_Address_Location)
    c.drawString(430, 280, personal_details.Name)
    c.drawString(430, 230, str(academic.dateadmission))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(230, 120, ' FOR OFFICE USE')
    c.drawString(150, 90, 'ADMISSION STATUS')
    c.drawString(150, 60, 'ADMITTED UNDER QUOTA')
    c.drawString(150, 30, 'BRANCH ALLOTTED ')
    c.drawString(280, 90, ':')
    c.drawString(285, 60, ':')
    c.drawString(280, 30, ':')
    c.setFont('Helvetica', 10)
    c.drawString(300, 90, 'ADMITTED')
    c.drawString(300, 60, personal_details.Quota)
    c.drawString(300, 30, personal_details.Department)




    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response



# ....................................................................... post_dip_voc....................................................................





def post_dip_voc(request,admissionNo):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=admissionNo)
    hsc = HSC_Marks.objects.get(admissionNo=admissionNo)
    academic = Academic_Details.objects.get(admissionNo=admissionNo)
    diplomo= Diplomo.objects.get(admissionNo=admissionNo)
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

    
    c.setFont('Helvetica-Bold', 10)
    c.rect(465, 660, 90, 30)
    c.drawRightString(455, 675, "Application from ")
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.setFont('Helvetica', 10)
    c.drawString(470, 675, personal_details.admissionFor)  
    c.drawString(470, 635, personal_details.Quota)  # Replace with the actual quota
    c.drawString(470, 595, personal_details.Department)  # Replace with the actual branch
    c.drawString(470, 555, personal_details.Mode)  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)
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
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 485, 'Name') 
    c.drawString(155, 485, ':') 
    c.drawString(30, 455, 'Sex ') 
    c.drawString(155, 455, ':') 

    c.drawString(30, 425, 'Date Of Birth ') 
    c.drawString(155, 425, ':') 

    c.drawString(30, 395, 'Age') 
    c.drawString(155, 395, ':') 

    c.drawString(30, 365, 'Nationality') 
    c.drawString(155, 365, ':') 

    c.drawString(30, 335, 'Religion') 
    c.drawString(155, 335, ':') 

    c.drawString(30, 305, 'Mother Tounge') 
    c.drawString(155, 305, ':') 

    c.drawString(30, 275, 'Nativity') 
    c.drawString(155, 275, ':') 

    c.drawString(30, 245, 'Self Mobile Number') 
    c.drawString(155, 245, ':') 

    c.drawString(30, 215, 'Self E - Mail ID') 
    c.drawString(155, 215, ':') 

    c.drawString(30, 185, 'Father Name') 
    c.drawString(155, 185, ':') 

    c.drawString(30, 155, 'Father Mobile Number') 
    c.drawString(155, 155, ':') 

    c.drawString(30, 125, 'Mother Name') 
    c.drawString(155, 125, ':') 

    c.drawString(30, 95, 'Mother Mobile Number') 
    c.drawString(155, 95, ':') 

    c.drawString(30, 65, 'Guardian Name') 
    c.drawString(155, 65, ':') 

    c.drawString(30, 35, 'Guardian Mobile Number') 
    c.drawString(155, 35, ':') 

    c.drawString(330, 485, 'Community') 
    c.drawString(400, 485, ':') 

    c.drawString(330, 455, 'Caste') 
    c.drawString(400, 455, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 485, personal_details.Name) 
    c.drawString(180, 455, personal_details.Gender) 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))
    c.drawString(180, 365, personal_details.Nationality) 
    c.drawString(180, 395, str(personal_details.Age)) 
    c.drawString(180, 335, personal_details.Religion) 
    c.drawString(180, 305, personal_details.Mother_Tongue) 
    c.drawString(180, 275, personal_details.Nativity) 
    c.drawString(180, 245, personal_details.Self_Mobile_Number) 
    c.drawString(180, 215, personal_details.Self_Mobile_Number) 
    c.drawString(180, 185, personal_details.Father_name) 
    c.drawString(180, 155, personal_details.Father_Mobile_Number) 
    c.drawString(180, 125, personal_details.Mother_name) 
    c.drawString(180, 95, personal_details.Mother_Mobile_Number) 
    c.drawString(180, 65, personal_details.Guardian_name) 
    c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 
    c.drawString(420, 485, personal_details.Community) 
    c.drawString(420, 455, personal_details.Caste) 




    c.showPage()
    c.drawCentredString(290, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'II. Communication Details')

    # Draw the rectangle
    c.rect(100, 522, 480, 260)
    c.line(100, 742, 580, 742)  # Horizontal line under the permanent address
    c.line(100, 712, 580, 712)
    c.line(100, 682, 580, 682)
    c.line(100, 652, 580, 652)
    c.line(100, 622, 580, 622)
    c.line(100, 592, 580, 592)
    c.line(100, 562, 580, 562)
    c.line(330, 782, 330, 520)  #   vertical

    # Set the font
    c.setFont('Helvetica-Bold', 13)

    # Place the value inside the rectangle
    c.drawString(130, 755, 'Permanent Address')
    c.drawString(390, 755, 'Communication Address')
    c.setFont('Helvetica', 11)
    c.drawString(170, 725, personal_details.Permanent_Address_Door_No) 
    c.drawString(140, 695, personal_details.Permanent_Address_Street_Name) 
    c.drawString(150, 665, personal_details.Permanent_Address_Location) 
    c.drawString(165, 635, personal_details.Permanent_Address_Pincode) 
    c.drawString(150, 605, personal_details.Permanent_Address_Taluk) 
    c.drawString(150, 575, personal_details.Permanent_Address_District) 
    c.drawString(150, 545, personal_details.Permanent_Address_State) 

    c.drawString(450, 725, personal_details.Communication_Address_Door_No) 
    c.drawString(420, 695, personal_details.Communication_Address_Street_Name) 
    c.drawString(430, 665, personal_details.Communication_Address_Location) 
    c.drawString(445, 635, personal_details.Communication_Address_Pincode) 
    c.drawString(420, 605, personal_details.Communication_Address_Taluk) 
    c.drawString(420, 575, personal_details.Communication_Address_District) 
    c.drawString(420, 545, personal_details.Communication_Address_State) 

    c.drawString(30, 725, 'Door No') 
    c.drawString(30, 695, 'Street Name') 
    c.drawString(30, 665, 'Location ') 
    c.drawString(30, 635, 'Pincode') 
    c.drawString(30, 605, 'Taluk ') 
    c.drawString(30, 575, 'District ') 
    c.drawString(30, 545, 'State') 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 483, 'III. Admission Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 453, '1. Counselling Application Number :')
    c.drawString(350, 453, '2. Management Application Number :')
    c.drawString(30, 423, '3. Counselling General Rank  :')
    c.drawString(350, 423, '4. Counselling Community Rank :')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number :')

    c.setFont('Helvetica', 10)
    c.drawString(230, 453, str(academic.Counselling_Application_No))
    c.drawString(530, 453, 'academic')
    c.drawString(230, 423, str(academic.Counselling_General_Rank))
    c.drawString(530, 423, 'academic')
    c.drawString(230, 393, str(academic.GQ_admissionNo))
    
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 343, 'IV. Academic Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 313, 'a. EMIS Number')
    c.setFont('Helvetica', 10)
    c.drawString(120, 313, personal_details.EMIS_ID)
    c.rect(30, 263, 550, 30)
    c.rect(30, 203, 550, 60)
    c.rect(30, 120, 550, 30)
    c.rect(30, 60, 550, 60)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 277, '10th Std. School Information')
    c.drawString(35, 247, 'Name of the Institution :')
    c.drawString(435, 247, 'Year Of Passing :')
    c.drawString(35, 217, 'Place of the Institution :')
    c.drawString(235, 217, 'Board of Study :')
    c.drawString(435, 217, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 247, personal_details.Tenth_Std_School_Name)
    c.drawString(525, 247, str(personal_details.Tenth_Std_Year_of_Passing))
    c.drawString(150, 217, personal_details.Tenth_Std_Place_of_School)
    c.drawString(315, 217, personal_details.Tenth_Std_School_Type)
    c.drawString(525, 217, personal_details.Tenth_Std_Medium_of_Study)


    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 135, '11th Std. School Information')
    c.drawString(35, 103, 'Name of the Institution :')
    c.drawString(435, 103, 'Year Of Passing :')
    c.drawString(35, 71, 'Place of the Institution :')
    c.drawString(235, 71, 'Category :')
    c.drawString(435, 71, 'Medium of Study :')

    c.setFont('Helvetica', 10)
    c.drawString(150, 103, hsc.Eleventh_Std_School_Name)
    c.drawString(525, 103, str(hsc.Eleventh_Std_Year_of_Passing))
    c.drawString(150, 71, hsc.Eleventh_Std_Place_of_School)
    c.drawString(285, 71, hsc.Eleventh_Std_Category)
    c.drawString(525, 71, hsc.Eleventh_Std_Medium_of_Study)
    # Build the PDF document
    # Save the PDF
    c.showPage()
    c.drawCentredString(290, 820, ":: 3 ::")
    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, '12th Std. School Information')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, hsc.Twelfth_Std_School_Name)
    c.drawString(525, 745, str(hsc.Twelfth_Std_Year_of_Passing))
    c.drawString(150, 715, hsc.Twelfth_Std_Place_of_School)
    c.drawString(285, 715, hsc.Twelfth_Std_Category)
    c.drawString(525, 715, hsc.Twelfth_Std_Medium_of_Study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.HSC Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'HSC Register Number :')
    c.drawString(50, 593, 'HSC Marksheet Number :')
    c.drawString(370, 623, 'HSC Studied In  :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, hsc.Twelfth_Std_Register_No)
    c.drawString(180, 593, hsc.Twelfth_Std_Marksheet_No)
    c.drawString(450, 623, hsc.Twelfth_Std_studied_in)


    c.rect(30, 543, 550, 30)
    c.rect(30, 363, 550, 180)
    c.line(290, 365, 290, 545) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 555, 'HSC Marks Scored in HSC Vocational ')
    c.drawString(70, 520, 'Language')
    c.drawString(70, 498, 'English')
    c.drawString(70, 473, 'Chemistry')
    c.drawString(70, 448, hsc.Twelfth_Std_voc_Mathematics_or_Physics_Name)
    c.drawString(70, 423, hsc.Twelfth_Std_voc_Vocational_Theory_Name)
    c.drawString(70, 398, 'Practical_Name')
    c.drawString(70, 373, 'Total')
    c.drawString(330, 398, 'Cutoff')
    c.drawString(330, 373, 'Percentage')
    c.drawString(140, 520, ':')
    c.drawString(140, 498, ':')
    c.drawString(140, 473, ':')
    c.drawString(140, 448, ':')
    c.drawString(140, 423, ':')
    c.drawString(140, 398, ':')
    c.drawString(140, 373, ':')
    c.drawString(390, 398, ':')
    c.drawString(390, 373, ':')
    c.setFont('Helvetica', 10)
    c.drawString(150, 520, str(hsc.Twelfth_Std_voc_Language_Mark))
    c.drawString(150, 498, str(hsc.Twelfth_Std_voc_English_Mark))
    c.drawString(150, 473, str(hsc.Twelfth_Std_voc_chemistry_Mark))
    c.drawString(150, 448, str(hsc.Twelfth_Std_voc_Mathematics_or_Physics_Mark))
    c.drawString(150, 423, str(hsc.Twelfth_Std_voc_Vocational_Theory_Mark))
    c.drawString(150, 398, str(hsc.Twelfth_Std_voc_Practical_Mark))
    c.drawString(150, 373, str(hsc.Twelfth_Std_voc_Total_Marks))
    c.drawString(400, 398, str(hsc.Twelfth_Std_voc_CUT_OFF_Mark))
    c.drawString(400, 373, str(hsc.Twelfth_Std_voc_PCM_Average))
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 333, 'VI. SSLC Details')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 303, 'SSLC Register Number :')
    c.drawString(50, 273, 'SSLC Marksheet Number :')
    c.drawString(370, 303, 'SSLC Studied In :')
    c.drawString(370, 273, 'SSLC Exam Number :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 303, personal_details.Tenth_Std_Register_No)
    c.drawString(180, 273, personal_details.Tenth_Std_Marksheet_No)
    c.drawString(470, 303, personal_details.Tenth_Std_Studied_In)
    c.drawString(470, 273, personal_details.Tenth_Std_Roll_No)

    c.rect(30, 223, 550, 30)
    c.rect(30, 43, 550, 180)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 232, 'SSLC Marks Scored in HSC Vocational ')
    c.drawString(215, 207, 'Tamil')
    c.drawString(215, 182, 'English')
    c.drawString(215, 157, 'Mathematics')
    c.drawString(215, 132, 'Science')
    c.drawString(215, 107, 'Social Science ')
    c.drawString(215, 82, 'N/A ')
    c.drawString(215, 57, 'Total')
    c.drawString(300, 207, ':')
    c.drawString(300, 182, ':')
    c.drawString(300, 157, ':')
    c.drawString(300, 132, ':')
    c.drawString(300, 107, ': ')
    c.drawString(300, 82, ':')
    c.drawString(300, 57, ':')
    c.setFont('Helvetica', 10)
    c.drawString(320, 207, str(personal_details.Tenth_Std_Tamil_Mark))
    c.drawString(320, 182, str(personal_details.Tenth_Std_English_Mark))
    c.drawString(320, 157, str(personal_details.Tenth_Std_Maths_Mark))
    c.drawString(320, 132, str(personal_details.Tenth_Std_Science_Mark))
    c.drawString(320, 107, str(personal_details.Tenth_Std_SocialScience_Mark))
    c.drawString(320, 82, str(personal_details.Tenth_Std_Others_Mark))
    c.drawString(320, 57, str(personal_details.Tenth_Std_Obtain_Mark))
    c.showPage()
    
    c.setFont('Helvetica-Bold', 13)
    c.rect(30, 763, 550, 30)
    c.rect(30, 703, 550, 60)

    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 775, 'Name_of_the_Polytechnic_College')
    c.drawString(35, 745, 'Name of the Institution :')
    c.drawString(435, 745, 'Year Of Passing :')
    c.drawString(35, 715, 'Place of the Institution :')
    c.drawString(235, 715, 'Category :')
    c.drawString(435, 715, 'Medium of Study :')
    c.setFont('Helvetica', 10)
    c.drawString(150, 745, diplomo.Name_of_the_Polytechnic_College)
    c.drawString(525, 745, str(diplomo.year_of_passing))
    c.drawString(150, 715, diplomo.Polytechnic_College_place)
    c.drawString(285, 715, diplomo.Diploma_apply_for)
    c.drawString(525, 715, diplomo.medium_of_study)

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 653, 'V.Diploma Details')

    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 623, 'diplomo Register Number :')
    c.drawString(420, 623, 'dip certificate No :')
    c.drawString(260, 623, 'diplomo Studied In  :')

    c.drawString(50, 593, 'dip total_percentages:')
    c.drawString(420, 593, 'dip total_mark:')
    c.drawString(260, 593, 'dip obtain_mark :')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, diplomo.diploma_register_no)
    c.drawString(510, 623, diplomo.diploma_certificate_no)
    c.drawString(370, 623, diplomo.diploma_studied_in)

    c.drawString(180, 593, diplomo.total_percentages)
    c.drawString(510, 593, diplomo.diploma_total_mark)
    c.drawString(370, 593, diplomo.diploma_obtain_mark)

    c.setFont('Helvetica-Bold', 13)
    c.line(150, 530, 150, 470)
    c.line(300, 530, 300, 470) 
    c.line(450, 530, 450, 470) 
 
    c.rect(30, 530, 550, 30)
    c.rect(30, 500, 550, 30)
    c.rect(30, 470, 550, 30)

    c.setFont('Helvetica-Bold', 10)

    c.drawString(215, 540, 'Diploma Marks Scored in Diploma ')

    c.drawString(70, 513, 'Sem3')
    c.drawString(210, 513, 'Sem4')
    c.drawString(360, 513, 'Sem5')
    c.drawString(500, 513, 'Sem6')

    c.setFont('Helvetica', 10)
    c.drawString(70, 483, diplomo.sem3_obtain_mark)
    c.drawString(210, 483, diplomo.sem4_obtain_mark)
    c.drawString(360, 483, diplomo.sem5_obtain_mark)
    c.drawString(500, 483, diplomo.sem6_obtain_mark)

    c.drawCentredString(290, 820, ":: 4 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 440, 'V. Special Reservation Information')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(330, 410, '5.Ex-Service Man Quota ') 
    c.drawString(330, 380, '6.Sports Quota ') 
    c.drawString(330, 350, '7.Differently abled Person Quota ') 
    c.drawString(330, 320, '8.PMSS (only SC/ST/SCA/SCC) ') 
    c.drawString(30, 410, '1.First Generation Graduate') 
    c.drawString(30, 380, '2.Certificate Number') 
    c.drawString(30, 350, "3.7.5% Govt. Quota") 
    c.drawString(30, 320, '4.Vocational') 

    c.drawString(500, 410, ':') 
    c.drawString(500, 380, ':') 
    c.drawString(500, 350, ':') 
    c.drawString(500, 320, ':') 
    c.drawString(200, 410, ':') 
    c.drawString(200, 380, ':') 
    c.drawString(200, 350, ':') 
    c.drawString(200, 320, ':') 
    c.setFont('Helvetica', 10)
    if academic.ScholarShip=='EX-SERVICE MAN QUOTA':
        ex='Yes'
    else:
        ex='N/A'
    c.drawString(230, 410, ex) 

    if academic.ScholarShip=='SPORTS QUOTA':
        sp='Yes'
    else:
        sp='N/A'

    if academic.ScholarShip=='DIFFERENTLY ABLED PERSON QUOTA':
        dfap='Yes'
    else:
        dfap='N/A'


    if academic.ScholarShip=='FIRST_GENERATION_GRADUATE':
        fg='Yes'
    else:
        fg='N/A'


    if academic.First_Graduate_certificate_No:
        fgc=academic.First_Graduate_certificate_No
    else:
        fgc='N/A'


    if academic.ScholarShip=='PMSS':
        pmss='Yes'
    else:
        pmss='N/A'

    if academic.ScholarShip=='GOVT_SCHOOL':
        gc='Yes'
    else:
        gc='N/A'

    if hsc.Twelfth_Std_Education_Qualified=='vocational':
        voc='Yes'
    else:
        voc='N/A'


    c.drawString(530, 380, sp) 
    c.drawString(530, 350, dfap) 
    c.drawString(530, 320, pmss) 
    c.drawString(530, 410, fg) 
    c.drawString(230, 380, fgc) 
    c.drawString(230, 350, gc) 
    c.drawString(230, 320, voc) 


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 290, 'VI. Occupation of Parent / Guardian')

    c.setFont('Helvetica', 10)
    c.rect(80, 240, 480, 30)
    c.rect(80, 210, 480, 30)
    c.line(190, 270, 190, 210) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 250, 'Occupation') 
    c.drawString(300, 220, 'Job Details') 
    c.setFont('Helvetica', 10)
    c.drawString(300, 250, academic.Occupation) 
    c.drawString(100, 220, academic.Job_Details) 

    c.drawString(30, 180, 'Family Annual Income of Parent / Guardian ') 
    c.drawString(30, 150, '(As per Income Certificate)') 

    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 130, 'VII. a) Scholarship Information : (Only GQ)')

    c.setFont('Helvetica', 10)
    c.rect(80, 80, 480, 30)
    c.rect(80, 50, 480, 30)
    c.rect(80, 20, 480, 30)
    c.line(190, 110, 190, 20) 
    c.line(470, 110, 470, 20) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(100, 90, 'Std') 
    c.drawString(300, 90, 'School Name') 
    c.drawString(490, 90, 'School Type') 
    c.setFont('Helvetica', 10)
    c.drawString(100, 60, '6th-10th') 
    c.drawString(300, 60, str(academic.Name_of_Std_6th_10th)) 
    c.drawString(490, 60, academic.Std_6th_10th_schooltype) 
    c.drawString(100, 30, '11th-12th') 
    c.drawString(300, 30, str(academic.School_Name_of_Std_11th_12th)) 
    c.drawString(490, 30, academic.Std_11th_12th_School_Type) 



    c.showPage()
    c.drawCentredString(290, 820, ":: 5 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'b) Student Bank Account Details :')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 770, 'Account Holder Name ') 
    c.drawString(30, 740, 'Name of the Bank ') 
    c.drawString(30, 710, 'Branch Name of the Bank') 
    c.drawString(30, 680, 'Branch Code Number') 
    c.drawString(30, 650, 'IFSC Code ') 
    c.drawString(30, 620, 'MICR Code ') 
    c.drawString(300, 770, 'Account Number ') 
    c.drawString(160, 770, ':') 
    c.drawString(160, 740, ':') 
    c.drawString(160, 710, ':') 
    c.drawString(160, 680, ':') 
    c.drawString(160, 650, ':') 
    c.drawString(160, 620, ':') 
    c.drawString(390, 770, ':') 
    c.setFont('Helvetica', 10)
    c.drawString(180, 770, academic.Bank_Holder_Name) 
    c.drawString(180, 740, academic.Name_of_the_Bank) 
    c.drawString(180, 710, academic.Branch_Name_of_the_Bank) 
    c.drawString(180, 680, academic.Branch_Code_No) 
    c.drawString(180, 650, academic.IFSC) 
    c.drawString(180, 620, academic.MICR) 
    c.drawString(400, 770, academic.Account_No) 
    c.setFont('Helvetica-Bold', 14)
    c.drawString(30, 590, 'JOINT DECLARATION BY THE APPLICANT AND PARENT / GUARDIAN')
    c.setFont('Helvetica', 10)
    c.drawString(30, 560, 'We hereby solemnly affirm that the information furnished by us in the Application form and also in the enclosure there to')
    c.drawString(30, 540, 'submitted by us are true. If any information furnished therein is untrue in material particulars or on verification at a later')
    c.drawString(30, 520, 'stage, we are liable for criminal prosecution and we also agree to forgo the seat in this Institution / for removal')
    c.drawString(30, 500, "of student's name from roll of the Institution at whatever the stage of study he/she may be at the time of detection")
    c.drawString(30, 480, 'of such wrong particulars. If admitted, we agree to abide by the rules and regulations of the Institution and submit')
    c.drawString(30, 460, 'the Anti-ragging Affidavits by the Student and by the Parent within 2 weeks from the date of commencement')
    c.drawString(30, 440, 'of the Semester / College reopening. In the event of any violation of the College rules / Hostel rules by the Student')
    c.drawString(30, 420, 'we agree to obey the action taken by the Institution.')


    c.setFont('Helvetica-Bold', 10)
    c.drawString(30, 350, 'Signature of the Parent / Guardian')
    c.drawString(330, 350, 'Signature of the Applicant')
    c.drawString(30, 280, 'Name')
    c.drawString(30, 230, 'Place')
    c.drawString(330, 280, 'Name')
    c.drawString(330, 230, 'Date of Admission ')

    c.drawString(70, 280, ':')
    c.drawString(70, 230, ':')
    c.drawString(420, 280, ':')
    c.drawString(420, 230, ':')
    c.setFont('Helvetica', 10)
    c.drawString(90, 280, personal_details.Father_name)
    c.drawString(90, 230, personal_details.Permanent_Address_Location)
    c.drawString(430, 280, personal_details.Name)
    c.drawString(430, 230, str(academic.dateadmission))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(230, 120, ' FOR OFFICE USE')
    c.drawString(150, 90, 'ADMISSION STATUS')
    c.drawString(150, 60, 'ADMITTED UNDER QUOTA')
    c.drawString(150, 30, 'BRANCH ALLOTTED ')
    c.drawString(280, 90, ':')
    c.drawString(285, 60, ':')
    c.drawString(280, 30, ':')
    c.setFont('Helvetica', 10)
    c.drawString(300, 90, 'ADMITTED')
    c.drawString(300, 60, personal_details.Quota)
    c.drawString(300, 30, personal_details.Department)




    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
    