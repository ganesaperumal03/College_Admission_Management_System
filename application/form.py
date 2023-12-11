from django import forms
from .models import Personal_Details,HSC_Marks,Academic_Details,Diplomo

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
        fields = ['EMIS_ID', 'Tenth_Std_School_Name', 'Tenth_Std_Year_of_Passing','Tenth_Std_Place_of_School', 'Tenth_Std_Medium_of_Study', 'Tenth_Std_School_Type','Tenth_Std_Register_No', 'Tenth_Std_Roll_No', 'Tenth_Std_Marksheet_No'
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
        exclude = ['admissionNo','personal'] 

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