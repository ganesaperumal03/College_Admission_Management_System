import random
from faker import Faker
from django.core.management.base import BaseCommand
from application.models import Personal_Details,HSC_Marks,Academic_Details,Diplomo
from django.http import HttpResponse

fake = Faker()
tenth=100
def populate_fake_data(request):
    print('Populating Personal_Details with fake data...')

    for _ in range(200):
           common_admission_no = fake.unique.random_number(digits=8)
           personal_instance=Personal_Details.objects.create(
                admissionNo=common_admission_no,
                admissionFor=fake.random_element(elements=('I_Year','I_Year')),
                Quota=fake.random_element(elements=('MQ', 'GQ')),
                Department=fake.random_element(elements=('B.TECH AD', 'B.E CIVIL', 'B.TECH CSBS', 'B.E CSE', 'B.E EEE', 'B.E ECE', 'B.TECH IT', 'B.E MECH')),
                Mode=fake.random_element(elements=('Hostel', 'Transport')),
                Name=fake.name(),
                Date_of_Birth=fake.date_of_birth(),
                Gender=fake.random_element(elements=('Male', 'Female')),
                Age=fake.random_int(min=18, max=30),
                Nationality=fake.country(),
                Religion=fake.random_element(elements=('Hindu', 'Muslim', 'Christian', 'Other')),
                Mother_Tongue=fake.random_element(elements=('Tamil', 'English', 'Hindi', 'Other')),
                Nativity=fake.random_element(elements=('Urban', 'Rural')),
                Self_Mobile_Number=fake.phone_number(),
                Self_Email_ID=fake.email(),
                Father_name=fake.name(),
                Father_Mobile_Number=fake.phone_number(),
                Mother_name=fake.name(),
                Mother_Mobile_Number=fake.phone_number(),
                Guardian_name=fake.name(),
                Guardian_Father_Mobile_No=fake.phone_number(),
                Community=fake.random_element(elements=('OC', 'BC', 'MBC', 'SC', 'ST')),
                Caste=fake.random_element(elements=('General', 'Reserved')),
                CommunityNumber=fake.random_number(digits=5),
                Aadhaar_Number=fake.random_number(digits=12),
                Profile_Image=fake.image_url(),
                Father_Profile_Image=fake.image_url(),
                Mother_Profile_Image=fake.image_url(),
                Signature_Image=fake.image_url(),

                Permanent_Address_Door_No=fake.building_number(),
                Permanent_Address_Street_Name=fake.street_name(),
                Permanent_Address_Location=fake.city(),
                Permanent_Address_Pincode=fake.zipcode(),
                Permanent_Address_Taluk=fake.city(),
                Permanent_Address_District=fake.city(),
                Permanent_Address_State=fake.state(),

                Communication_Address_Door_No=fake.building_number(),
                Communication_Address_Street_Name=fake.street_name(),
                Communication_Address_Location=fake.city(),
                Communication_Address_Pincode=fake.zipcode(),
                Communication_Address_Taluk=fake.city(),
                Communication_Address_District=fake.city(),
                Communication_Address_State=fake.state(),

                EMIS_ID=fake.random_number(digits=8),
                Tenth_Std_School_Name=fake.company(),
                Tenth_Std_Year_of_Passing=fake.year(),
                Tenth_Std_Place_of_School=fake.city(),
                Tenth_Std_Medium_of_Study=fake.random_element(elements=('Tamil', 'English')),
                Tenth_Std_School_Type=fake.random_element(elements=('Government', 'Private')),
                Tenth_Std_Register_No=fake.random_number(digits=10),
                Tenth_Std_Roll_No=fake.random_number(digits=10),
                Tenth_Std_Marksheet_No=fake.random_number(digits=10),
                Tenth_Std_Studied_In=fake.random_element(elements=('Regular', 'Matriculation', 'CBSE')),

                Tenth_Std_Tamil_Name=fake.random_element(elements=('Tamil',)),
                Tenth_Std_Tamil_Mark=fake.random_number(digits=2),
                Tenth_Std_Tamil_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_English_Name=fake.random_element(elements=('English',)),
                Tenth_Std_English_Mark=fake.random_number(digits=2),
                Tenth_Std_English_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_Maths_Name=fake.random_element(elements=('Mathematics',)),
                Tenth_Std_Maths_Mark=fake.random_number(digits=2),
                Tenth_Std_Maths_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_Science_Name=fake.random_element(elements=('Science',)),
                Tenth_Std_Science_Mark=fake.random_number(digits=2),
                Tenth_Std_Science_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_SocialScience_Name=fake.random_element(elements=('Social Science',)),
                Tenth_Std_SocialScience_Mark=fake.random_number(digits=2),
                Tenth_Std_SocialScience_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_Others_Name=fake.random_element(elements=('Other Subject',)),
                Tenth_Std_Others_Mark=fake.random_number(digits=2),
                Tenth_Std_Others_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_Obtain_Mark=fake.random_number(digits=2),
                Tenth_Std_Total_Mark=tenth,
                # GQ_MQ_Converted=fake.random_element(elements=('GQ', 'MQ')),
                # Dept_Changed=fake.random_element(elements=('Yes', 'No')),

            )

           academic_instance=Academic_Details.objects.create(
                personal=personal_instance,
                admissionNo=common_admission_no,
                Counselling_Application_No=fake.random_number(digits=4),
                GQ_Admission_Number=fake.random_number(digits=4),
                Counselling_General_Rank=fake.random_number(digits=4),
                ScholarShip=fake.random_element(elements=('Yes', 'No')),
                First_Graduate_certificate_No=fake.random_number(digits=7),
                govper=fake.random_element(elements=('Yes', 'No')),
                Occupation=fake.random_element(elements=('Student', 'Employee', 'Self-Employed')),
                Job_Details=fake.job(),
                Annual_Income=fake.random_number(digits=6),
                Name_of_Std_6th_10th=fake.name(),
                Std_6th_10th_schooltype=fake.random_element(elements=('Government', 'Private')),
                School_Name_of_Std_11th_12th=fake.company(),
                Std_11th_12th_School_Type=fake.random_element(elements=('Government', 'Private')),
                Name_of_the_Bank=fake.company(),
                Branch_Name_of_the_Bank=fake.company_suffix(),
                Branch_Code_No=fake.random_number(digits=6),
                IFSC=fake.random_element(elements=('IFSC1234', 'IFSC5678')),
                MICR=fake.random_number(digits=9),
                Bank_Holder_Name=fake.name(),
                Account_No=fake.random_number(digits=12),
                How=fake.random_element(elements=('Entrance Exam', 'Direct Admission')),
                dateadmission=fake.date_of_birth(minimum_age=17, maximum_age=30),
                admission_Category=fake.random_element(elements=('General', 'SC', 'ST', 'OBC')),
            )
           hsc_instance=HSC_Marks.objects.create(
                personal=personal_instance,

                admissionNo=common_admission_no,
                
                Eleventh_Std_School_Name=fake.company(),
                Eleventh_Std_Year_of_Passing=fake.random_int(min=2010, max=2022),
                Eleventh_Std_Place_of_School=fake.city(),
                Eleventh_Std_Medium_of_Study=fake.random_element(elements=('Tamil', 'English')),
                Eleventh_Std_Category=fake.random_element(elements=('Regular', 'Matriculation', 'CBSE')),

                # 12th Std Details
                Twelfth_Std_School_Name=fake.company(),
                Twelfth_Std_Year_of_Passing=fake.random_int(min=2010, max=2022),
                Twelfth_Std_Place_of_School=fake.city(),
                Twelfth_Std_Medium_of_Study=fake.random_element(elements=('Tamil', 'English')),
                Twelfth_Std_Category=fake.random_element(elements=('Regular', 'Matriculation', 'CBSE')),
                Twelfth_Std_Register_No=fake.random_number(digits=10),
                Twelfth_Std_Marksheet_No=fake.random_number(digits=10),
                Twelfth_Std_studied_in=fake.random_element(elements=('Regular', 'Matriculation', 'CBSE')),
                Twelfth_Std_Education_Qualified=fake.random_element(elements=('aca', 'voc')),

                # 12th Std Academic Details
                Twelfth_Std_aca_Language_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_English_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_Mathematics_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_Physics_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_Chemistry_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_Elective_Name=fake.random_element(elements=('Biology', 'Computer Science')),
                Twelfth_Std_aca_Elective_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_Total_Marks=fake.random_number(digits=2),
                Twelfth_Std_aca_CUT_OFF_Mark=fake.random_number(digits=2),
                Twelfth_Std_aca_PCM_Average=fake.pyfloat(left_digits=2, right_digits=2, positive=True),

                # 12th Std Vocational Details
                Twelfth_Std_voc_Language_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_English_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_chemistry_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_Mathematics_or_Physics_Name=fake.random_element(elements=('Biology', 'Computer Science')),
                Twelfth_Std_voc_Mathematics_or_Physics_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_Vocational_Theory_Name=fake.random_element(elements=('Computer Science', 'Business Studies')),
                Twelfth_Std_voc_Vocational_Theory_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_Practical_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_Total_Marks=fake.random_number(digits=2),
                Twelfth_Std_voc_CUT_OFF_Mark=fake.random_number(digits=2),
                Twelfth_Std_voc_PCM_Average=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            )
           Diplomo.objects.create(
                personal=personal_instance,
                admissionNo=common_admission_no,
                Name_of_the_Polytechnic_College=fake.company(),
                Polytechnic_College_place=fake.city(),
                Diploma_apply_for=fake.random_element(elements=('Diploma_Iyear', 'Diploma_IIyear')),
                medium_of_study=fake.random_element(elements=('English', 'Tamil')),
                year_of_passing=fake.random_int(min=2010, max=2023),
                diploma_register_no=fake.random_number(digits=10),
                diploma_certificate_no=fake.random_number(digits=10),
                diploma_studied_in=fake.random_element(elements=('Government', 'Private')),
                education_qualified=fake.random_element(elements=('Yes', 'No')),
                sem1_total_mark=fake.random_number(digits=3),
                sem1_obtain_mark=fake.random_number(digits=3),
                sem2_total_mark=fake.random_number(digits=3),
                sem2_obtain_mark=fake.random_number(digits=3),
                sem3_total_mark=fake.random_number(digits=3),
                sem3_obtain_mark=fake.random_number(digits=3),
                sem4_total_mark=fake.random_number(digits=3),
                sem4_obtain_mark=fake.random_number(digits=3),
                sem5_total_mark=fake.random_number(digits=3),
                sem5_obtain_mark=fake.random_number(digits=3),
                sem6_total_mark=fake.random_number(digits=3),
                sem6_obtain_mark=fake.random_number(digits=3),
                total_percentages=fake.random_number(digits=2),
                diploma_total_mark=fake.random_number(digits=4),
                diploma_obtain_mark=fake.random_number(digits=4),
            )



    return HttpResponse('Fake data generated successfully!')