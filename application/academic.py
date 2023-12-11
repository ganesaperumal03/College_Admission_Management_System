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
from .models import Personal_Details, HSC_Marks, Academic_Details
from PIL import Image, ImageFilter
import os
import base64

def create_pdf(request):
    # Create an in-memory PDF file
    personal_details = get_object_or_404(Personal_Details, admissionNo=2327001)
    hsc = HSC_Marks.objects.get(admissionNo=2327001)
    academic = Academic_Details.objects.get(admissionNo=2327001)

    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="example.pdf"'
    document = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Create PDF
    c = canvas.Canvas(buffer, pagesize=A4)

    # Set font
    c.setFont('Helvetica', 10)


    c.drawCentredString(270, 820, ":: 1 ::")
    c.drawRightString(530, 820, "App No :")
    c.drawRightString(570, 820, str(personal_details.admissionNo)) 
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

    # Drawing rectangles for photos


    # Labeling the rectangles
    # c.drawCentredString(27.5, 655, 'Affix\nPassport Size\nPhoto')
    # c.drawCentredString(67.5, 655, 'Affix\nPassport Size\nPhoto')
    # c.drawCentredString(107.5, 655, 'Affix\nPassport Size\nPhoto')

    # End of photo details

    # Other primary details
    c.rect(465, 660, 90, 30)
    c.drawRightString(455, 675, "Application from ")
    c.drawString(470, 675, personal_details.admissionFor)  
    # Replace with the actual application type
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    c.drawString(470, 635, personal_details.Quota)  # Replace with the actual quota
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    c.drawString(470, 595, personal_details.Department)  # Replace with the actual branch
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.drawString(470, 555, personal_details.Mode)  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)

    def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            # Read binary data from the image file
            binary_data = image_file.read()

            # Encode the binary data to Base64
            base64_data = base64.b64encode(binary_data).decode('utf-8')

        return base64_data

    image_path = personal_details.Profile_Image.path  
    base64_encoded_image = image_to_base64(image_path)

    binary_data = base64.b64decode(base64_encoded_image)

    image_file = BytesIO(binary_data)

    img = Image.open(image_file)

    max_width = 90
    max_height = 130

    img = img.resize((max_width, max_height), Image.LANCZOS)
    img_reader = ImageReader(img)

    img_width, img_height = img.size

    c.drawImage(img_reader, 30, 545, width=img_width, height=img_height)


    image_path = personal_details.Father_Profile_Image.path  
    base64_encoded_image = image_to_base64(image_path)

    binary_data = base64.b64decode(base64_encoded_image)

    image_file = BytesIO(binary_data)

    img = Image.open(image_file)

    max_width = 90
    max_height = 130

    img = img.resize((max_width, max_height), Image.LANCZOS)
    img_reader = ImageReader(img)

    img_width, img_height = img.size

    c.drawImage(img_reader, 150, 545, width=img_width, height=img_height)

    image_path = personal_details.Mother_Profile_Image.path  
    base64_encoded_image = image_to_base64(image_path)

    binary_data = base64.b64decode(base64_encoded_image)

    image_file = BytesIO(binary_data)

    img = Image.open(image_file)

    max_width = 90
    max_height = 130

    img = img.resize((max_width, max_height), Image.LANCZOS)
    img_reader = ImageReader(img)

    img_width, img_height = img.size

    c.drawImage(img_reader, 270, 545, width=img_width, height=img_height)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Helvetica', 10)
    c.drawString(30, 485, 'Name') 
    c.drawString(180, 485, personal_details.Name) 

    c.drawString(30, 455, 'Sex ') 
    c.drawString(180, 455, personal_details.Gender) 

    c.drawString(30, 425, 'Date Of Birth ') 
    c.drawString(180, 425, str(personal_details.Date_of_Birth))

    c.drawString(30, 395, 'Age') 
    c.drawString(180, 395, str(personal_details.Age)) 

    c.drawString(30, 365, 'Nationality') 
    c.drawString(180, 365, personal_details.Nationality) 

    c.drawString(30, 335, 'Religion') 
    c.drawString(180, 335, personal_details.Religion) 

    c.drawString(30, 305, 'Mother Tounge') 
    c.drawString(180, 305, personal_details.Mother_Tongue) 

    c.drawString(30, 275, 'Nativity') 
    c.drawString(180, 275, personal_details.Nativity) 

    c.drawString(30, 245, 'Self Mobile Number') 
    c.drawString(180, 245, personal_details.Self_Mobile_Number) 

    c.drawString(30, 215, 'Self E - Mail ID') 
    c.drawString(180, 215, personal_details.Self_Mobile_Number) 

    c.drawString(30, 185, 'Father Name') 
    c.drawString(180, 185, personal_details.Father_name) 

    c.drawString(30, 155, 'Father Mobile Number') 
    c.drawString(180, 155, personal_details.Father_Mobile_Number) 


    c.drawString(30, 125, 'Mother Name') 
    c.drawString(180, 125, personal_details.Mother_name) 

    c.drawString(30, 95, 'Mother Mobile Number') 
    c.drawString(180, 95, personal_details.Mother_Mobile_Number) 

    c.drawString(30, 65, 'Guardian Name') 
    c.drawString(180, 65, personal_details.Guardian_name) 

    c.drawString(30, 35, 'Guardian Mobile Number') 
    c.drawString(180, 35, personal_details.Guardian_Father_Mobile_No) 

    c.drawString(330, 485, 'Community') 
    c.drawString(420, 485, personal_details.Community) 

    c.drawString(330, 455, 'Caste') 
    c.drawString(420, 455, personal_details.Caste) 



    c.showPage()
    c.drawCentredString(270, 820, ":: 2 ::")
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
    c.drawString(132, 575, personal_details.Permanent_Address_District) 
    c.drawString(140, 545, personal_details.Permanent_Address_State) 

    c.drawString(450, 725, personal_details.Communication_Address_Door_No) 
    c.drawString(420, 695, personal_details.Communication_Address_Street_Name) 
    c.drawString(430, 665, personal_details.Communication_Address_Location) 
    c.drawString(445, 635, personal_details.Communication_Address_Pincode) 
    c.drawString(420, 605, personal_details.Communication_Address_Taluk) 
    c.drawString(410, 575, personal_details.Communication_Address_District) 
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
    c.drawString(30, 423, '3. Counselling General Rank ')
    c.drawString(350, 423, '4. Counselling Community Rank')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number')

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
    c.drawCentredString(270, 820, ":: 3 ::")
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
    c.drawString(50, 623, 'HSC Register Number')
    c.drawString(50, 593, 'HSC Marksheet Number')
    c.drawString(370, 623, 'HSC Studied In ')

    c.setFont('Helvetica', 10)
    c.drawString(180, 623, hsc.Twelfth_Std_Register_No)
    c.drawString(180, 593, hsc.Twelfth_Std_Marksheet_No)
    c.drawString(450, 623, hsc.Twelfth_Std_studied_in)


    c.rect(30, 543, 550, 30)
    c.rect(30, 363, 550, 180)
    c.line(290, 365, 290, 545) 
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 555, 'HSC Marks Scored in HSC Academic ')
    c.drawString(50, 520, 'Language')
    c.drawString(50, 498, 'English')
    c.drawString(50, 473, 'Mathematics')
    c.drawString(50, 448, 'Physics')
    c.drawString(50, 423, 'Chemistry')
    c.drawString(50, 398, 'Biology')
    c.drawString(50, 373, 'Total')
    c.setFont('Helvetica', 10)
    c.drawString(120, 520, str(hsc.Twelfth_Std_aca_Language_Mark))
    c.drawString(120, 498, str(hsc.Twelfth_Std_aca_English_Mark))
    c.drawString(120, 473, str(hsc.Twelfth_Std_aca_Mathematics_Mark))
    c.drawString(120, 448, str(hsc.Twelfth_Std_aca_Physics_Mark))
    c.drawString(120, 423, str(hsc.Twelfth_Std_aca_Chemistry_Mark))
    c.drawString(120, 398, str(hsc.Twelfth_Std_aca_Elective_Mark))
    c.drawString(120, 373, str(hsc.Twelfth_Std_aca_Total_Marks))

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 333, 'VI. SSLC Details')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(50, 303, 'SSLC Register Number')
    c.drawString(50, 273, 'SSLC Marksheet Number')
    c.drawString(370, 303, 'SSLC Studied In')
    c.drawString(370, 273, 'SSLC Exam Number')

    c.setFont('Helvetica', 10)
    c.drawString(180, 303, personal_details.Tenth_Std_Register_No)
    c.drawString(180, 273, personal_details.Tenth_Std_Marksheet_No)
    c.drawString(470, 303, personal_details.Tenth_Std_Studied_In)
    c.drawString(470, 273, personal_details.Tenth_Std_Roll_No)

    c.rect(30, 223, 550, 30)
    c.rect(30, 43, 550, 180)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(215, 232, 'SSLC Marks Scored in HSC Academic ')
    c.drawString(230, 207, 'Tamil')
    c.drawString(230, 182, 'English')
    c.drawString(230, 157, 'Mathematics')
    c.drawString(230, 132, 'Science')
    c.drawString(230, 107, 'Social Science ')
    c.drawString(230, 82, 'N/A ')
    c.drawString(230, 57, 'Total')
    c.setFont('Helvetica', 10)
    c.drawString(320, 207, str(personal_details.Tenth_Std_Tamil_Mark))
    c.drawString(320, 182, str(personal_details.Tenth_Std_English_Mark))
    c.drawString(320, 157, str(personal_details.Tenth_Std_Maths_Mark))
    c.drawString(320, 132, str(personal_details.Tenth_Std_Science_Mark))
    c.drawString(320, 107, str(personal_details.Tenth_Std_SocialScience_Mark))
    c.drawString(320, 82, str(personal_details.Tenth_Std_Others_Mark))
    c.drawString(320, 57, str(personal_details.Tenth_Std_Obtain_Mark))
    c.showPage()
    c.drawCentredString(270, 820, ":: 4 ::")
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

    c.setFont('Helvetica', 10)
    c.drawString(230, 760, 'N/A') 
    c.drawString(230, 730, 'N/A') 
    c.drawString(230, 700, 'N/A') 
    c.drawString(230, 670, 'N/A') 
    c.drawString(230, 640, 'N/A') 
    c.drawString(230, 610, 'N/A') 
    c.drawString(230, 580, 'N/A') 
    c.drawString(230, 550, 'N/A') 


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
    c.drawString(300, 440, 'Job Details') 
    c.drawString(100, 440, 'Job Details') 

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
    c.drawString(30, 180, 'Account Holder Name :') 
    c.drawString(30, 150, 'Name of the Bank :') 
    c.drawString(30, 120, 'Branch Name of the Bank :') 
    c.drawString(30, 90, 'Branch Code Number :') 
    c.drawString(30, 60, 'IFSC Code :') 
    c.drawString(30, 30, 'MICR Code :') 
    c.drawString(280, 180, 'Account Number :') 

    c.setFont('Helvetica', 10)
    c.drawString(180, 180, academic.Bank_Holder_Name) 
    c.drawString(180, 150, academic.Name_of_the_Bank) 
    c.drawString(180, 120, academic.Branch_Name_of_the_Bank) 
    c.drawString(180, 90, academic.Branch_Code_No) 
    c.drawString(180, 60, academic.IFSC) 
    c.drawString(180, 30, academic.MICR) 
    c.drawString(380, 180, academic.Account_No) 

    c.showPage()
    c.drawCentredString(270, 820, ":: 5 ::")
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
    c.setFont('Helvetica', 10)
    c.drawString(90, 450, personal_details.Father_name)
    c.drawString(90, 410, personal_details.Permanent_Address_Location)
    c.drawString(430, 450, personal_details.Name)
    c.drawString(430, 410, str(academic.dateadmission))


    c.setFont('Helvetica-Bold', 10)
    c.drawString(230, 200, ' FOR OFFICE USE')
    c.drawString(150, 160, 'ADMISSION STATUS')
    c.drawString(150, 120, 'ADMITTED UNDER QUOTA')
    c.drawString(150, 80, 'BRANCH ALLOTTED ')
    c.setFont('Helvetica', 10)
    c.drawString(300, 160, 'ADMITTED')
    c.drawString(300, 120, personal_details.Quota)
    c.drawString(300, 80, personal_details.Department)




    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response