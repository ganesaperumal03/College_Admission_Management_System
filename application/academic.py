from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# Register the Arial font
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'arial.ttf')) 
def create_pdf(request):
    # Create an in-memory PDF file
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="example.pdf"'
    document = SimpleDocTemplate(buffer, pagesize=letter)
    # Create PDF
    c = canvas.Canvas(buffer, pagesize=A4)

    # Set font
    c.setFont('Helvetica', 10)


    # Set font
    c.setFont('Helvetica', 10)

    c.drawCentredString(270, 820, ":: 1 ::")
    c.drawRightString(530, 820, "App No :")
    c.drawRightString(570, 820, "123456")  # Replace with the actual admission number

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
    c.drawString(470, 675, "Engineering")  
    # Replace with the actual application type
    c.rect(465, 620, 90, 30)
    c.drawRightString(455, 635, "Quota ")
    c.drawString(470, 635, "Management")  # Replace with the actual quota
    
    c.rect(465, 580, 90, 30)
    c.drawRightString(455, 595, "Branch Alloted ")
    c.drawString(470, 595, "Computer Science")  # Replace with the actual branch
    
    c.rect(465, 540, 90, 30)
    c.drawRightString(455, 555, "Mode ")
    c.drawString(470, 555, "Regular")  # Replace with actual data

    c.rect(30, 545, 90, 130)
    c.rect(150, 545, 90, 130)
    c.rect(270, 545, 90, 130)



# personal

    c.drawString(30, 515, 'I. Personal Details') 

    c.setFont('Arial', 10)
    c.drawString(30, 485, 'Name ') 
    c.drawString(160, 485, 'name') 

    c.drawString(30, 455, 'Sex ') 
    c.drawString(160, 455, 'name') 

    c.drawString(30, 415, 'Date Of Birth ') 
    c.drawString(160, 415, 'name') 

    c.drawString(30, 385, 'Age') 
    c.drawString(160, 485, 'name') 

    c.drawString(30, 355, 'Nationality') 
    c.drawString(160, 455, 'name') 

    c.drawString(30, 315, 'Religion') 
    c.drawString(160, 425, 'name') 

    c.drawString(30, 285, 'Mother Tounge') 
    c.drawString(160, 395, 'name') 

    c.drawString(30, 255, 'Nativity') 
    c.drawString(160, 365, 'name') 

    c.drawString(30, 215, 'Self Mobile Number') 
    c.drawString(160, 335, 'name') 

    c.drawString(30, 185, 'Self E - Mail ID') 
    c.drawString(160, 305, 'name') 

    c.drawString(30, 155, 'Father Name') 
    c.drawString(160, 275, 'name') 

    c.drawString(30, 115, 'Father Mobile Number') 
    c.drawString(160, 245, 'name') 


    c.drawString(30, 85, 'Mother Name') 
    c.drawString(160, 215, 'name') 

    c.drawString(30, 55, 'Mother Mobile Number') 
    c.drawString(160, 185, 'name') 

    c.drawString(30, 145, 'Guardian Name') 
    c.drawString(160, 155, 'name') 

    c.drawString(30, 115, 'Guardian Mobile Number') 
    c.drawString(160, 125, 'name') 

    c.drawString(30, 85, 'Community') 
    c.drawString(160, 95, 'name') 

    c.drawString(30, 55, 'Caste') 
    c.drawString(160, 65, 'name') 



    c.showPage()
    c.drawCentredString(270, 820, ":: 2 ::")
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 800, 'II. Communication Details')

    # Draw the rectangle
    c.rect(100, 522, 480, 260)

    # Set the font
    c.setFont('Helvetica-Bold', 13)

    # Place the value inside the rectangle
    c.drawString(130, 755, 'Permanent Address')
    c.drawString(390, 755, 'Communication Address')
    c.setFont('Arial', 11)
    c.drawString(170, 725, '5/107') 
    c.drawString(140, 695, 'Bazanai Kovil Street ') 
    c.drawString(150, 665, 'Natchiyarpatti ') 
    c.drawString(165, 635, '626135') 
    c.drawString(150, 605, 'Rajapalayam ') 
    c.drawString(132, 575, 'VIRUDHUNAGAR ') 
    c.drawString(140, 545, 'TAMIL NADU ') 

    c.drawString(450, 725, '5/107') 
    c.drawString(420, 695, 'Bazanai Kovil Street ') 
    c.drawString(430, 665, 'Natchiyarpatti ') 
    c.drawString(445, 635, '626135') 
    c.drawString(420, 605, 'Rajapalayam ') 
    c.drawString(410, 575, 'VIRUDHUNAGAR ') 
    c.drawString(420, 545, 'TAMIL NADU ') 

    c.drawString(30, 725, 'Door No') 
    c.drawString(30, 695, 'Street Name') 
    c.drawString(30, 665, 'Location ') 
    c.drawString(30, 635, 'Pincode') 
    c.drawString(30, 605, 'Taluk ') 
    c.drawString(30, 575, 'District ') 
    c.drawString(30, 545, 'State') 

    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 483, 'III. Admission Details')

    c.setFont('Helvetica', 10)
    c.drawString(30, 453, '1. Counselling Application Number :')
    c.drawString(350, 453, '2. Management Application Number :')
    c.drawString(30, 423, '3. Counselling General Rank ')
    c.drawString(350, 423, '4. Counselling Community Rank')
    c.drawString(30, 393, '5. GQ Seat Allotment Order Number')
    
    
    c.setFont('Helvetica-Bold', 13)
    c.drawString(30, 343, 'IV. Academic Information')
    c.setFont('Helvetica', 10)
    c.drawString(30, 313, 'a. EMIS Number')
    c.drawString(120, 313, '1001586656')
    c.rect(30, 263, 550, 30)
    c.rect(30, 203, 550, 60)

    c.rect(30, 120, 550, 30)
    c.rect(30, 60, 550, 60)
    # Build the PDF document
    # Save the PDF
    c.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response