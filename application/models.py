from django.db import models

from datetime import datetime
year = int(datetime.now().strftime("%Y"))
class Personal_Details(models.Model):
    admissionNo = models.CharField(max_length=20, primary_key=True)
    admissionFor = models.CharField(max_length=100)
    Quota = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Mode = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    Gender = models.CharField(max_length=10)
    Age = models.IntegerField()
    Nationality = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50)
    Mother_Tongue = models.CharField(max_length=50)
    Nativity = models.CharField(max_length=50)
    Self_Mobile_Number = models.CharField(max_length=15)
    Self_Email_ID = models.EmailField()
    Father_name = models.CharField(max_length=100)
    Father_Mobile_Number = models.CharField(max_length=15)
    Mother_name = models.CharField(max_length=100)
    Mother_Mobile_Number = models.CharField(max_length=15)
    Guardian_name = models.CharField(max_length=100,blank=True,null=True)
    Guardian_Father_Mobile_No = models.CharField(max_length=15,blank=True,null=True)
    Community = models.CharField(max_length=50)
    Caste = models.CharField(max_length=50)
    CommunityNumber = models.CharField(max_length=20)
    Aadhaar_Number = models.CharField(max_length=20)
    Profile_Image =  models.ImageField(upload_to='profile_images/')
    Father_Profile_Image = models.ImageField(upload_to='profile_images/')
    Mother_Profile_Image = models.ImageField(upload_to='profile_images/')
    Signature_Image = models.ImageField(upload_to='profile_images/')


    # Permanent Address
    Permanent_Address_Door_No = models.CharField(max_length=20)
    Permanent_Address_Street_Name = models.CharField(max_length=100)
    Permanent_Address_Location = models.CharField(max_length=100)
    Permanent_Address_Pincode = models.CharField(max_length=10)
    Permanent_Address_Taluk = models.CharField(max_length=50)
    Permanent_Address_District = models.CharField(max_length=50)
    Permanent_Address_State = models.CharField(max_length=50)

    # Communication Address
    Communication_Address_Door_No = models.CharField(max_length=20)
    Communication_Address_Street_Name = models.CharField(max_length=100)
    Communication_Address_Location = models.CharField(max_length=100)
    Communication_Address_Pincode = models.CharField(max_length=10)
    Communication_Address_Taluk = models.CharField(max_length=50)
    Communication_Address_District = models.CharField(max_length=50)
    Communication_Address_State = models.CharField(max_length=50)


    # 10th Std Details
 
    EMIS_ID=models.CharField(max_length=100,blank=True,null=True)


    Tenth_Std_School_Name = models.CharField(max_length=100)
    other_Tenth_Std_School_Name = models.CharField(max_length=100,blank=True,null=True)

    Tenth_Std_Year_of_Passing = models.CharField(max_length=100)
    Tenth_Std_Place_of_School = models.CharField(max_length=100)
    Tenth_Std_Medium_of_Study = models.CharField(max_length=50)
    Tenth_Std_School_Type = models.CharField(max_length=50)
    Tenth_Std_Register_No = models.CharField(max_length=20)
    Tenth_Std_Roll_No = models.CharField(max_length=20)
    Tenth_Std_Marksheet_No = models.CharField(max_length=20)
    Tenth_Std_Studied_In = models.CharField(max_length=50)
    
    # Subjects and Marks
    Tenth_Std_Tamil_Name = models.CharField(max_length=100)
    Tenth_Std_Tamil_Mark = models.CharField(max_length=50)
    Tenth_Std_Tamil_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_English_Name = models.CharField(max_length=100)
    Tenth_Std_English_Mark = models.CharField(max_length=50)
    Tenth_Std_English_Obtain_Mark =models.CharField(max_length=50)
    Tenth_Std_Maths_Name = models.CharField(max_length=100)
    Tenth_Std_Maths_Mark = models.CharField(max_length=50)
    Tenth_Std_Maths_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_Science_Name = models.CharField(max_length=100)
    Tenth_Std_Science_Mark = models.CharField(max_length=50)
    Tenth_Std_Science_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_SocialScience_Name = models.CharField(max_length=100)
    Tenth_Std_SocialScience_Mark = models.CharField(max_length=50)
    Tenth_Std_SocialScience_Obtain_Mark =models.CharField(max_length=50)
    Tenth_Std_Others_Name = models.CharField(max_length=100,blank=True,null=True)
    Tenth_Std_Others_Mark = models.IntegerField(blank=True,null=True)
    Tenth_Std_Others_Obtain_Mark = models.IntegerField(blank=True,null=True) 
    Tenth_Std_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_Total_Mark = models.CharField(max_length=50)
    GQ_MQ_Converted = models.CharField(max_length=100,blank=True,null=True)
    Dept_Changed = models.CharField(max_length=100,blank=True,null=True)
    admission_exit = models.CharField(max_length=50,blank=True,null=True)
    academic_Category = models.CharField(max_length=50,blank=True,null=True)


    # Other Details
    def __str__(self):
        return self.admissionNo


class HSC_Marks(models.Model):
    personal = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    admissionNo = models.CharField(max_length=20)
    Eleventh_Std_School_Name = models.CharField(max_length=100)
    other_Eleventh_Std_School_Name = models.CharField(max_length=100,blank=True,null=True)

    Eleventh_Std_Year_of_Passing = models.IntegerField()
    Eleventh_Std_Place_of_School = models.CharField(max_length=100)
    Eleventh_Std_Medium_of_Study = models.CharField(max_length=50)
    Eleventh_Std_Category = models.CharField(max_length=50)

    # 12th Std Details
    Twelfth_Std_School_Name = models.CharField(max_length=100)
    other_Twelfth_Std_School_Name = models.CharField(max_length=100,blank=True,null=True)

    Twelfth_Std_Year_of_Passing = models.IntegerField()
    Twelfth_Std_Place_of_School = models.CharField(max_length=100)
    Twelfth_Std_Medium_of_Study = models.CharField(max_length=50)
    Twelfth_Std_Category = models.CharField(max_length=50)
    
    Twelfth_Std_Register_No = models.CharField(max_length=20)
    Twelfth_Std_Marksheet_No = models.CharField(max_length=20)
    Twelfth_Std_studied_in = models.CharField(max_length=50)
    Twelfth_Std_Education_Qualified = models.CharField(max_length=50)

    # 12th Std Academic Details
    Twelfth_Std_aca_Language_Mark = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_English_Mark = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_Mathematics_Mark = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_Physics_Mark = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_Chemistry_Mark = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_Elective_Name = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_Elective_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_aca_Total_Marks = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_aca_CUT_OFF_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_aca_PCM_Average = models.CharField(max_length=50,blank=True,null=True)

    # 12th Std Vocational Details
    Twelfth_Std_voc_Language_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_English_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_chemistry_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_Mathematics_or_Physics_Name = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_Mathematics_or_Physics_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_Vocational_Theory_Name = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_Vocational_Theory_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_Practical_Mark = models.CharField(max_length=50,blank=True,null=True)

    Twelfth_Std_voc_Total_Marks = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_CUT_OFF_Mark = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_voc_PCM_Average = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.admissionNo


class Academic_Details(models.Model):
    personal = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    admissionNo = models.CharField(max_length=20)
    Counselling_Application_No = models.CharField(max_length=100,blank=True,null=True)
    GQ_Admission_Number = models.CharField(max_length=100,blank=True,null=True)
    Counselling_General_Rank = models.CharField(max_length=100,blank=True,null=True)
    ScholarShip = models.CharField(max_length=100,blank=True,null=True)
    First_Graduate_certificate_No = models.CharField(max_length=100,blank=True,null=True)
    govper = models.CharField(max_length=100,blank=True,null=True)
    Occupation = models.CharField(max_length=50)
    Job_Details = models.CharField(max_length=100)
    Annual_Income = models.CharField(max_length=50)
    Name_of_Std_6th_10th = models.CharField(max_length=100,blank=True,null=True)
    Std_6th_10th_schooltype = models.CharField(max_length=50,blank=True,null=True)
    School_Name_of_Std_11th_12th = models.CharField(max_length=100,blank=True,null=True)
    Std_11th_12th_School_Type = models.CharField(max_length=50,blank=True,null=True)
    Name_of_the_Bank = models.CharField(max_length=100)
    Branch_Name_of_the_Bank = models.CharField(max_length=100)
    Branch_Code_No = models.CharField(max_length=20)
    IFSC = models.CharField(max_length=20)
    MICR = models.CharField(max_length=20)
    Bank_Holder_Name = models.CharField(max_length=100)
    Account_No = models.CharField(max_length=20)
    How = models.CharField(max_length=100)
    dateadmission = models.DateField()
    admission_Category = models.CharField(max_length=50,blank=True,null=True)
    academic_year = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Set academic_year to the current year if not provided
        if not self.academic_year:
            self.academic_year = str(datetime.now().year)
        super(Academic_Details, self).save(*args, **kwargs)
    def __str__(self):
        return self.admissionNo

from django.db import models

class Diplomo(models.Model):
    personal = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    admissionNo = models.CharField(max_length=20)
    Name_of_the_Polytechnic_College= models.CharField(max_length=100)
    Polytechnic_College_place= models.CharField(max_length=100)
    Diploma_apply_for=models.CharField(max_length=50)
    medium_of_study = models.CharField(max_length=50)
    year_of_passing = models.CharField(max_length=50)
    diploma_register_no = models.CharField(max_length=50)
    diploma_certificate_no = models.CharField(max_length=50)
    diploma_studied_in = models.CharField(max_length=50, )
    education_qualified = models.CharField(max_length=50)
    sem1_total_mark = models.CharField(max_length=5)
    sem1_obtain_mark = models.CharField(max_length=5)
    sem2_total_mark = models.CharField(max_length=5)
    sem2_obtain_mark = models.CharField(max_length=5)
    sem3_total_mark = models.CharField(max_length=5)
    sem3_obtain_mark = models.CharField(max_length=5)
    sem4_total_mark = models.CharField(max_length=5)
    sem4_obtain_mark = models.CharField(max_length=5)
    sem5_total_mark = models.CharField(max_length=5)
    sem5_obtain_mark = models.CharField(max_length=5)
    sem6_total_mark = models.CharField(max_length=5)
    sem6_obtain_mark = models.CharField(max_length=5)
    total_percentages = models.CharField(max_length=5)
    diploma_total_mark = models.CharField(max_length=5)
    diploma_obtain_mark = models.CharField(max_length=5)

    def __str__(self):
        return self.admissionNo
    

class Preform(models.Model):
    Name = models.CharField(max_length=100)
    admissionNo = models.CharField(max_length=20,primary_key=True)
    Date_of_Birth = models.DateField()
    Quota = models.CharField(max_length=50)
    Department = models.CharField(max_length=50,blank=True,null=True)
    Branch_Preferrence_1 = models.CharField(max_length=100)
    Branch_Preferrence_2 = models.CharField(max_length=100)
    ad_preferrence = models.CharField(max_length=10)
    civil_preferrence = models.CharField(max_length=10)
    csbs_preferrence = models.CharField(max_length=10)
    cse_preferrence = models.CharField(max_length=10)
    eee_preferrence = models.CharField(max_length=10)
    ece_preferrence = models.CharField(max_length=10)
    it_preferrence = models.CharField(max_length=10)
    mech_preferrence = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    Father_name = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=50)
    Community = models.CharField(max_length=50)
    Residental_Address_Line_1= models.CharField(max_length=50)
    Residental_Address_Line_2= models.CharField(max_length=50)
    Self_Mobile_Number = models.CharField(max_length=15)
    Father_Mobile_Number = models.CharField(max_length=15)
    Nationality = models.CharField(max_length=50)
    Self_Email_ID = models.EmailField()
    Aadhaar_Number = models.CharField(max_length=50)
    Profile_Image = models.ImageField(upload_to=" 'personal_profile_images/', year",blank=True,null=True)
    Physically_Challenged = models.CharField(max_length=100,blank=True,null=True)
    First_Generation_Graduate = models.CharField(max_length=100,blank=True,null=True)
    Hostel_Required = models.CharField(max_length=100,blank=True,null=True)
    UPI_Ref_No = models.CharField(max_length=50,blank=True,null=True)
    admission_exit = models.CharField(max_length=50,blank=True,null=True)

    date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.admissionNo

class Preform_other_info(models.Model):
    personal = models.ForeignKey(Preform, on_delete=models.CASCADE)
    admissionNo = models.CharField(max_length=20)
    admissionFor = models.CharField(max_length=100)
    Tenth_Std_School_Name = models.CharField(max_length=100)
    Tenth_Std_Register_No = models.CharField(max_length=20)
    Tenth_Std_Medium_of_Study = models.CharField(max_length=50)
    Tenth_Std_Year_of_Passing = models.CharField(max_length=50)
    Tenth_Std_Place_of_School = models.CharField(max_length=50,blank=True,null=True)
    Tenth_Std_School_Type = models.CharField(max_length=50)


    
    Tenth_Std_Tamil_Name = models.CharField(max_length=100)
    Tenth_Std_Tamil_Mark = models.CharField(max_length=50)
    Tenth_Std_Tamil_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_English_Name = models.CharField(max_length=100)
    Tenth_Std_English_Mark = models.CharField(max_length=50)
    Tenth_Std_English_Obtain_Mark =models.CharField(max_length=50)
    Tenth_Std_Maths_Name = models.CharField(max_length=100)
    Tenth_Std_Maths_Mark = models.CharField(max_length=50)
    Tenth_Std_Maths_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_Science_Name = models.CharField(max_length=100)
    Tenth_Std_Science_Mark = models.CharField(max_length=50)
    Tenth_Std_Science_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_SocialScience_Name = models.CharField(max_length=100)
    Tenth_Std_SocialScience_Mark = models.CharField(max_length=50)
    Tenth_Std_SocialScience_Obtain_Mark =models.CharField(max_length=50)
    Tenth_Std_Others_Name = models.CharField(max_length=100,blank=True,null=True)
    Tenth_Std_Others_Mark = models.IntegerField(blank=True,null=True)
    Tenth_Std_Others_Obtain_Mark = models.IntegerField(blank=True,null=True) 
    Tenth_Std_Obtain_Mark = models.CharField(max_length=50)
    Tenth_Std_Total_Mark = models.CharField(max_length=50)
    diploma = models.CharField(max_length=50,blank=True,null=True)
    YEAR_OF_ADMISSION = models.CharField(max_length=100)

    Twelfth_Std_School_Name = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_Year_of_Passing = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_Place_of_School = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_Medium_of_Study = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_studied_in = models.CharField(max_length=50,blank=True,null=True)
    Twelfth_Std_Education_Qualified = models.CharField(max_length=50,blank=True,null=True)

    # 12th Std Academic Details
    Twelfth_Std_aca_Language_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_English_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_Mathematics_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_Physics_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_Chemistry_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_Elective_Name = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_aca_Elective_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_Total_Marks = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_CUT_OFF_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_aca_PCM_Average = models.FloatField(blank=True,null=True)

    # 12th Std Vocational Details
    Twelfth_Std_voc_Language_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_English_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_chemistry_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_Mathematics_or_Physics_Name = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_voc_Mathematics_or_Physics_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_Vocational_Theory_Name = models.CharField(max_length=100,blank=True,null=True)
    Twelfth_Std_voc_Vocational_Theory_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_Practical_Mark = models.IntegerField(blank=True,null=True)

    Twelfth_Std_voc_Total_Marks = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_CUT_OFF_Mark = models.IntegerField(blank=True,null=True)
    Twelfth_Std_voc_PCM_Average = models.FloatField(blank=True,null=True)
   

    Name_of_the_Polytechnic_College= models.CharField(max_length=100)
    Polytechnic_College_place= models.CharField(max_length=100)
    Diploma_apply_for=models.CharField(max_length=50)
    medium_of_study = models.CharField(max_length=50)
    year_of_passing = models.CharField(max_length=50)
    diploma_register_no = models.CharField(max_length=50)
    diploma_certificate_no = models.CharField(max_length=50)
    diploma_studied_in = models.CharField(max_length=50, )
    sem1_total_mark = models.CharField(max_length=5)
    sem1_obtain_mark = models.CharField(max_length=5)
    sem2_total_mark = models.CharField(max_length=5)
    sem2_obtain_mark = models.CharField(max_length=5)
    sem3_total_mark = models.CharField(max_length=5)
    sem3_obtain_mark = models.CharField(max_length=5)
    sem4_total_mark = models.CharField(max_length=5)
    sem4_obtain_mark = models.CharField(max_length=5)
    sem5_total_mark = models.CharField(max_length=5)
    sem5_obtain_mark = models.CharField(max_length=5)
    sem6_total_mark = models.CharField(max_length=5)
    sem6_obtain_mark = models.CharField(max_length=5)
    total_percentages = models.CharField(max_length=5)
    diploma_total_mark = models.CharField(max_length=5)
    diploma_obtain_mark = models.CharField(max_length=5)
    Department = models.CharField(max_length=50,blank=True,null=True)

    admission_exit = models.CharField(max_length=50,blank=True,null=True)


    def __str__(self):
        return self.admissionNo
    

class Personalform(models.Model):
    Name = models.CharField(max_length=100)
    admissionNo = models.CharField(max_length=20,primary_key=True)
    year = models.CharField(max_length=50,blank=True,null=True)
    Quota = models.CharField(max_length=50)
    Department = models.CharField(max_length=50,blank=True,null=True)
    Gender = models.CharField(max_length=10)
    Father_name = models.CharField(max_length=100,blank=True,null=True)
    place= models.CharField(max_length=50)
    Mobile_Number = models.CharField(max_length=15,blank=True,null=True)
    Aadhaar_Number = models.CharField(max_length=50)
    cutoffmark = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    gm_conform = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.admissionNo
    

class MQ_Fees(models.Model):
    Year = models.CharField(max_length=100)
    Department  = models.CharField(max_length=50)
    Tuition_Fees  = models.CharField(max_length=50)
    CoExtra_Curricularfees  = models.CharField(max_length=50)
    Development_fees  = models.CharField(max_length=50)
    Learning_Materials_Platform_UniformFees  = models.CharField(max_length=50)
    Caution_Deposit  = models.CharField(max_length=50)
    Hostel  = models.CharField(max_length=50,blank=True,null=True)
    Dayscholar  = models.CharField(max_length=50,blank=True,null=True)

class GQ_Fees(models.Model):
    Year = models.CharField(max_length=100)
    Department  = models.CharField(max_length=50)
    Tuition_Fees  = models.CharField(max_length=50)
    CoExtra_Curricularfees  = models.CharField(max_length=50)
    Development_fees  = models.CharField(max_length=50)
    Learning_Materials_Platform_UniformFees  = models.CharField(max_length=50)
    Caution_Deposit  = models.CharField(max_length=50)
    Hostel  = models.CharField(max_length=50,blank=True,null=True)
    Dayscholar  = models.CharField(max_length=50,blank=True,null=True)


class certificates(models.Model):
    admissionNo = models.CharField(max_length=20,primary_key=True)
    Tenth_mark_sheet = models.BooleanField(default=False)
    eleventh_mark_sheet = models.BooleanField(default=False)
    Twelfth_mark_sheet = models.BooleanField(default=False)
    Transfer_Certificate = models.BooleanField(default=False)
    Community_Certificate = models.BooleanField(default=False)
    First_year_graduate_Certificate = models.BooleanField(default=False)
    Income_Certificate = models.BooleanField(default=False)
    Migration_Certificate = models.BooleanField(default=False)
    
class transport(models.Model):
    admissionNo = models.CharField(max_length=20,primary_key=True)
    Bus_route = models.CharField(max_length=100,blank=True,null=True)
    Bus_stop = models.CharField(max_length=100,blank=True,null=True)
    Bus_no = models.CharField(max_length=100,blank=True,null=True)
    Bus_time = models.CharField(max_length=100,blank=True,null=True)

