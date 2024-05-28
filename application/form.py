from django import forms
from .models import Personal_Details,HSC_Marks,Academic_Details,Diplomo,Preform_other_info,Preform,Personalform,certificates,transport,user
# forms.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

class AdmissionPersonal(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = [
            'admissionNo', 'admissionFor', 'Quota', 'Department', 'Mode', 'Name', 'Date_of_Birth', 'Gender', 'Age',
            'Nationality', 'Religion', 'Mother_Tongue', 'Nativity', 'Self_Mobile_Number', 'Self_Email_ID',
            'Father_name', 'Father_Mobile_Number', 'Mother_name', 'Mother_Mobile_Number', 'Guardian_name',
            'Guardian_Father_Mobile_No', 'Community', 'Caste', 'CommunityNumber', 'Aadhaar_Number']
        
        # Exclude admissionNo, as it is generated separately
        exclude = ['admissionNo']
        
class Admissionaddress(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['Permanent_Address_Door_No', 'Permanent_Address_Street_Name', 'Permanent_Address_Location','Permanent_Address_Pincode', 'Permanent_Address_Taluk', 'Permanent_Address_District','Permanent_Address_State', 'Communication_Address_Door_No', 'Communication_Address_Street_Name'
        ,'Communication_Address_Location', 'Communication_Address_Pincode', 'Communication_Address_Taluk','Communication_Address_District',
         'Communication_Address_State']

class Admissionsslc(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['EMIS_ID', 'Tenth_Std_School_Name', "other_Tenth_Std_School_Name",'Tenth_Std_Year_of_Passing','Tenth_Std_Place_of_School', 'Tenth_Std_Medium_of_Study', 'Tenth_Std_School_Type','Tenth_Std_Register_No', 'Tenth_Std_Roll_No', 'Tenth_Std_Marksheet_No'
        ,'Tenth_Std_Studied_In', 'Tenth_Std_Tamil_Name', 'Tenth_Std_Tamil_Mark','Tenth_Std_Tamil_Obtain_Mark', 'Tenth_Std_English_Name','Tenth_Std_English_Mark', 'Tenth_Std_English_Obtain_Mark', 'Tenth_Std_Maths_Name','Tenth_Std_Maths_Mark', 'Tenth_Std_Maths_Obtain_Mark', 'Tenth_Std_Science_Name','Tenth_Std_Science_Mark', 'Tenth_Std_Science_Obtain_Mark', 'Tenth_Std_SocialScience_Name'
        ,'Tenth_Std_SocialScience_Mark', 'Tenth_Std_SocialScience_Obtain_Mark', 'Tenth_Std_Others_Name','Tenth_Std_Others_Mark', 'Tenth_Std_Others_Obtain_Mark', 'Tenth_Std_Obtain_Mark',
         'Tenth_Std_Total_Mark']


class AdmissionMark(forms.ModelForm):
    class Meta:
        model = HSC_Marks
        fields = '__all__'
        exclude = ['admissionNo','personal'] 


class AdmissionDiploma(forms.ModelForm):
    class Meta:
        model = Diplomo
        fields = '__all__'
        exclude = ['admissionNo','personal', 'sem1_total_mark'  ,'sem1_obtain_mark', 'sem2_total_mark', 'sem2_obtain_mark'] 

class academic_Details(forms.ModelForm):
    class Meta:
        model = Academic_Details
        fields = '__all__'
        exclude = ['admissionNo','personal'] 


class quota_changed(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['Quota','GQ_MQ_Converted']

class dep_changed(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['Department','Dept_Changed']

class dep_changed(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['Department']

class preform_quota_changed(forms.ModelForm):
    class Meta:
        model = Preform
        fields = ['Quota']

class preform_dep_changed(forms.ModelForm):
    class Meta:
        model = Preform
        fields = ['Department']


class AdmissionPerform(forms.ModelForm):
    class Meta:
        model = Preform
        fields = [
            'Name', 'admissionNo', 'Date_of_Birth', 'Gender',
            'Nationality', 'Occupation', 'Residental_Address_Line_1', 'Self_Mobile_Number', 'Self_Email_ID',
            'Father_name', 'Father_Mobile_Number', 'Residental_Address_Line_2', 'Aadhaar_Number', 'Community']
        # Exclude admissionNo, as it is generated separately
        exclude = ['admissionNo']
        
class Perform_sslc(forms.ModelForm):
    class Meta:
        model = Preform_other_info
        fields = [ 'admissionNo','admissionFor', 'Tenth_Std_School_Name', 'Tenth_Std_Register_No','Tenth_Std_Medium_of_Study', 'Tenth_Std_Tamil_Name', 'Tenth_Std_Tamil_Mark','Tenth_Std_Tamil_Obtain_Mark', 'Tenth_Std_English_Name', 'Tenth_Std_English_Mark','Tenth_Std_English_Obtain_Mark'
        ,'Tenth_Std_Maths_Name', 'Tenth_Std_Maths_Mark', 'Tenth_Std_Maths_Obtain_Mark','Tenth_Std_Science_Name','Tenth_Std_Science_Mark','Tenth_Std_Science_Obtain_Mark','Tenth_Std_SocialScience_Name','Tenth_Std_SocialScience_Mark','Tenth_Std_SocialScience_Obtain_Mark','Tenth_Std_Others_Name','Tenth_Std_Others_Mark','Tenth_Std_Others_Obtain_Mark','Tenth_Std_Obtain_Mark',
         'Tenth_Std_Total_Mark','diploma', 'admissionNo', 'YEAR_OF_ADMISSION', 'Twelfth_Std_School_Name', 'Twelfth_Std_Year_of_Passing', 'Twelfth_Std_Place_of_School','Tenth_Std_Year_of_Passing','Tenth_Std_School_Type','Tenth_Std_Place_of_School',
            'Twelfth_Std_Medium_of_Study', 'Twelfth_Std_studied_in', 'Twelfth_Std_Education_Qualified', 'Twelfth_Std_aca_Language_Mark', 'Twelfth_Std_aca_English_Mark',
            'Twelfth_Std_aca_Mathematics_Mark', 'Twelfth_Std_aca_Physics_Mark', 'Twelfth_Std_aca_Chemistry_Mark', 'Twelfth_Std_aca_Elective_Name', 'Twelfth_Std_aca_Total_Marks',
            'Twelfth_Std_aca_Elective_Name', 'Twelfth_Std_aca_Elective_Mark', 'Twelfth_Std_aca_Elective_Mark', 'Twelfth_Std_aca_Elective_Mark', 'Twelfth_Std_aca_Elective_Mark', 'Twelfth_Std_aca_Elective_Mark', 'Twelfth_Std_aca_Elective_Mark'
            , 'Twelfth_Std_aca_CUT_OFF_Mark', 'Twelfth_Std_aca_PCM_Average', 'Twelfth_Std_voc_Language_Mark', 'Twelfth_Std_voc_English_Mark', 'Twelfth_Std_voc_chemistry_Mark', 'Twelfth_Std_voc_Mathematics_or_Physics_Name', 'Twelfth_Std_voc_Mathematics_or_Physics_Mark'
            , 'Twelfth_Std_voc_Vocational_Theory_Name', 'Twelfth_Std_voc_Vocational_Theory_Mark', 'Twelfth_Std_voc_Practical_Mark', 'Twelfth_Std_voc_Total_Marks', 'Twelfth_Std_voc_CUT_OFF_Mark', 'Twelfth_Std_voc_PCM_Average']
        

        exclude = ['admissionNo']

        
class Perform_diploma(forms.ModelForm):
    class Meta:
        model = Preform_other_info
        fields = ['Name_of_the_Polytechnic_College', 'Polytechnic_College_place', 'Diploma_apply_for','medium_of_study', 'year_of_passing', 'diploma_register_no','diploma_certificate_no', 'diploma_studied_in', 'sem1_total_mark'
        ,'sem1_obtain_mark', 'sem2_total_mark', 'sem2_obtain_mark', 'sem3_total_mark', 'sem3_obtain_mark', 'sem4_total_mark', 'sem4_obtain_mark', 'sem5_total_mark', 'sem5_obtain_mark',
         'sem6_total_mark', 'sem6_obtain_mark', 'sem2_total_mark', 'sem2_obtain_mark','total_percentages','diploma_total_mark','diploma_obtain_mark']
        exclude = [ 'sem1_total_mark'  ,'sem1_obtain_mark', 'sem2_total_mark', 'sem2_obtain_mark']


class Perform_declare(forms.ModelForm):
    class Meta:
        model = Preform
        fields = [ 'Physically_Challenged', 'Hostel_Required', 'First_Generation_Graduate', 'Quota','UPI_Ref_No','ad_preferrence','civil_preferrence','csbs_preferrence','cse_preferrence','eee_preferrence','ece_preferrence','it_preferrence','mech_preferrence']


class AdmissionPersonalform(forms.ModelForm):
    class Meta:
        model = Personalform
        fields = [
            'Name', 'admissionNo', 'year', 'Gender',
             'place', 'Mobile_Number', "Department",
            'Father_name', 'Aadhaar_Number',"Quota","cutoffmark"]
        # Exclude admissionNo, as it is generated separately
        exclude = ['admissionNo']

class personalformconform(forms.ModelForm):
    class Meta:
        model = Personalform
        fields = ['gm_conform']

class certificateform(forms.ModelForm):
    class Meta:
        model = certificates
        fields = [
            'admissionNo', 'Tenth_mark_sheet', 'eleventh_mark_sheet', 'Twelfth_mark_sheet',
             'Transfer_Certificate', 'Community_Certificate', "First_year_graduate_Certificate",
            'Income_Certificate', 'Migration_Certificate','Name','Department','Quota','admissionFor']
        exclude = ['admissionNo','Name','Department','Quota','admissionFor']

class transportform(forms.ModelForm):
    class Meta:
        model = transport
        fields = ['Bus_route','Bus_stop']


class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Name','username',"email","Role","password1","password2"]


class image_form(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['Profile_Image', 'Father_Profile_Image'
            ,'Mother_Profile_Image', 'Signature_Image']
        exclude = ['Profile_Image', 'Father_Profile_Image'
            ,'Mother_Profile_Image', 'Signature_Image']
