# Generated by Django 4.2.5 on 2023-12-11 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Details',
            fields=[
                ('admissionNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('admissionFor', models.CharField(max_length=100)),
                ('Quota', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Mode', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Date_of_Birth', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Nationality', models.CharField(max_length=50)),
                ('Religion', models.CharField(max_length=50)),
                ('Mother_Tongue', models.CharField(max_length=50)),
                ('Nativity', models.CharField(max_length=50)),
                ('Self_Mobile_Number', models.CharField(max_length=15)),
                ('Self_Email_ID', models.EmailField(max_length=254)),
                ('Father_name', models.CharField(max_length=100)),
                ('Father_Mobile_Number', models.CharField(max_length=15)),
                ('Mother_name', models.CharField(max_length=100)),
                ('Mother_Mobile_Number', models.CharField(max_length=15)),
                ('Guardian_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Guardian_Father_Mobile_No', models.CharField(max_length=15, null=True)),
                ('Community', models.CharField(max_length=50)),
                ('Caste', models.CharField(max_length=50)),
                ('CommunityNumber', models.CharField(max_length=20)),
                ('Aadhaar_Number', models.CharField(max_length=20)),
                ('Profile_Image', models.ImageField(upload_to='profile_images/')),
                ('Father_Profile_Image', models.ImageField(upload_to='profile_images/')),
                ('Mother_Profile_Image', models.ImageField(upload_to='profile_images/')),
                ('Signature_Image', models.ImageField(upload_to='profile_images/')),
                ('Permanent_Address_Door_No', models.CharField(max_length=20)),
                ('Permanent_Address_Street_Name', models.CharField(max_length=100)),
                ('Permanent_Address_Location', models.CharField(max_length=100)),
                ('Permanent_Address_Pincode', models.CharField(max_length=10)),
                ('Permanent_Address_Taluk', models.CharField(max_length=50)),
                ('Permanent_Address_District', models.CharField(max_length=50)),
                ('Permanent_Address_State', models.CharField(max_length=50)),
                ('Communication_Address_Door_No', models.CharField(max_length=20)),
                ('Communication_Address_Street_Name', models.CharField(max_length=100)),
                ('Communication_Address_Location', models.CharField(max_length=100)),
                ('Communication_Address_Pincode', models.CharField(max_length=10)),
                ('Communication_Address_Taluk', models.CharField(max_length=50)),
                ('Communication_Address_District', models.CharField(max_length=50)),
                ('Communication_Address_State', models.CharField(max_length=50)),
                ('EMIS_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Tenth_Std_School_Name', models.CharField(max_length=100)),
                ('Tenth_Std_Year_of_Passing', models.CharField(max_length=100)),
                ('Tenth_Std_Place_of_School', models.CharField(max_length=100)),
                ('Tenth_Std_Medium_of_Study', models.CharField(max_length=50)),
                ('Tenth_Std_School_Type', models.CharField(max_length=50)),
                ('Tenth_Std_Register_No', models.CharField(max_length=20)),
                ('Tenth_Std_Roll_No', models.CharField(max_length=20)),
                ('Tenth_Std_Marksheet_No', models.CharField(max_length=20)),
                ('Tenth_Std_Studied_In', models.CharField(max_length=50)),
                ('Tenth_Std_Tamil_Name', models.CharField(max_length=100)),
                ('Tenth_Std_Tamil_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Tamil_Obtain_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_English_Name', models.CharField(max_length=100)),
                ('Tenth_Std_English_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_English_Obtain_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Maths_Name', models.CharField(max_length=100)),
                ('Tenth_Std_Maths_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Maths_Obtain_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Science_Name', models.CharField(max_length=100)),
                ('Tenth_Std_Science_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Science_Obtain_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_SocialScience_Name', models.CharField(max_length=100)),
                ('Tenth_Std_SocialScience_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_SocialScience_Obtain_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Others_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Tenth_Std_Others_Mark', models.IntegerField(blank=True, null=True)),
                ('Tenth_Std_Others_Obtain_Mark', models.IntegerField(blank=True, null=True)),
                ('Tenth_Std_Obtain_Mark', models.CharField(max_length=50)),
                ('Tenth_Std_Total_Mark', models.CharField(max_length=50)),
                ('GQ_MQ_Converted', models.CharField(blank=True, max_length=100, null=True)),
                ('Dept_Changed', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HSC_Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionNo', models.CharField(max_length=20)),
                ('Eleventh_Std_School_Name', models.CharField(max_length=100)),
                ('Eleventh_Std_Year_of_Passing', models.IntegerField()),
                ('Eleventh_Std_Place_of_School', models.CharField(max_length=100)),
                ('Eleventh_Std_Medium_of_Study', models.CharField(max_length=50)),
                ('Eleventh_Std_Category', models.CharField(max_length=50)),
                ('Twelfth_Std_School_Name', models.CharField(max_length=100)),
                ('Twelfth_Std_Year_of_Passing', models.IntegerField()),
                ('Twelfth_Std_Place_of_School', models.CharField(max_length=100)),
                ('Twelfth_Std_Medium_of_Study', models.CharField(max_length=50)),
                ('Twelfth_Std_Category', models.CharField(max_length=50)),
                ('Twelfth_Std_Register_No', models.CharField(max_length=20)),
                ('Twelfth_Std_Marksheet_No', models.CharField(max_length=20)),
                ('Twelfth_Std_studied_in', models.CharField(max_length=50)),
                ('Twelfth_Std_Education_Qualified', models.CharField(max_length=50)),
                ('Twelfth_Std_aca_Language_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_English_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_Mathematics_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_Physics_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_Chemistry_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_Elective_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Twelfth_Std_aca_Elective_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_Total_Marks', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_CUT_OFF_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_aca_PCM_Average', models.FloatField(blank=True, null=True)),
                ('Twelfth_Std_voc_Language_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_English_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_chemistry_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_Mathematics_or_Physics_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Twelfth_Std_voc_Mathematics_or_Physics_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_Vocational_Theory_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Twelfth_Std_voc_Vocational_Theory_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_Practical_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_Total_Marks', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_CUT_OFF_Mark', models.IntegerField(blank=True, null=True)),
                ('Twelfth_Std_voc_PCM_Average', models.FloatField(blank=True, null=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.personal_details')),
            ],
        ),
        migrations.CreateModel(
            name='Diplomo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionNo', models.CharField(max_length=20)),
                ('Name_of_the_Polytechnic_College', models.CharField(max_length=100)),
                ('Polytechnic_College_place', models.CharField(max_length=100)),
                ('Diploma_apply_for', models.CharField(max_length=50)),
                ('medium_of_study', models.CharField(max_length=50)),
                ('year_of_passing', models.IntegerField()),
                ('diploma_register_no', models.CharField(max_length=50)),
                ('diploma_certificate_no', models.CharField(max_length=50)),
                ('diploma_studied_in', models.CharField(max_length=50)),
                ('education_qualified', models.CharField(max_length=50)),
                ('sem1_total_mark', models.CharField(max_length=5)),
                ('sem1_obtain_mark', models.CharField(max_length=5)),
                ('sem2_total_mark', models.CharField(max_length=5)),
                ('sem2_obtain_mark', models.CharField(max_length=5)),
                ('sem3_total_mark', models.CharField(max_length=5)),
                ('sem3_obtain_mark', models.CharField(max_length=5)),
                ('sem4_total_mark', models.CharField(max_length=5)),
                ('sem4_obtain_mark', models.CharField(max_length=5)),
                ('sem5_total_mark', models.CharField(max_length=5)),
                ('sem5_obtain_mark', models.CharField(max_length=5)),
                ('sem6_total_mark', models.CharField(max_length=5)),
                ('sem6_obtain_mark', models.CharField(max_length=5)),
                ('total_percentages', models.CharField(max_length=5)),
                ('diploma_total_mark', models.CharField(max_length=5)),
                ('diploma_obtain_mark', models.CharField(max_length=5)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.personal_details')),
            ],
        ),
        migrations.CreateModel(
            name='Academic_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionNo', models.CharField(max_length=20)),
                ('Counselling_Application_No', models.CharField(blank=True, max_length=100, null=True)),
                ('GQ_Admission_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Counselling_General_Rank', models.CharField(blank=True, max_length=100, null=True)),
                ('ScholarShip', models.CharField(blank=True, max_length=100, null=True)),
                ('First_Graduate_certificate_No', models.CharField(blank=True, max_length=100, null=True)),
                ('govper', models.CharField(blank=True, max_length=100, null=True)),
                ('Occupation', models.CharField(max_length=50)),
                ('Job_Details', models.CharField(max_length=100)),
                ('Annual_Income', models.CharField(max_length=50)),
                ('Name_of_Std_6th_10th', models.CharField(blank=True, max_length=100, null=True)),
                ('Std_6th_10th_schooltype', models.CharField(blank=True, max_length=50, null=True)),
                ('School_Name_of_Std_11th_12th', models.CharField(blank=True, max_length=100, null=True)),
                ('Std_11th_12th_School_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Name_of_the_Bank', models.CharField(max_length=100)),
                ('Branch_Name_of_the_Bank', models.CharField(max_length=100)),
                ('Branch_Code_No', models.CharField(max_length=20)),
                ('IFSC', models.CharField(max_length=20)),
                ('MICR', models.CharField(max_length=20)),
                ('Bank_Holder_Name', models.CharField(max_length=100)),
                ('Account_No', models.CharField(max_length=20)),
                ('How', models.CharField(max_length=100)),
                ('dateadmission', models.DateField()),
                ('admission_Category', models.CharField(blank=True, max_length=50, null=True)),
                ('admission_exit', models.CharField(blank=True, max_length=50, null=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.personal_details')),
            ],
        ),
    ]