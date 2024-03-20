from django import forms
from .models import registration

#creating a class for the form models

class Student_form(forms.ModelForm):
    class Meta:
        model = registration
        # fields = ['number','FirstName','LastName','Course','Email','Date']
        fields = '__all__'
        
        labels = {
            'FirstName':'Student Name',
            'LastName':'Student Last Name',
            'Course':'Student Course',
            'Email':'Student Email',
            'Phone_number':'Student phone number',
            'State_of_Origin': 'Student State of origin',
            'Date_of_birth': 'Student Date of birth',
            'Registration_Date': 'Student Registration Date',
            'Starting_Date': 'Student Starting Date',
            'Ending_Date': 'Student Ending Date',
            'Address':'Student address'
        }
        
        widgets = {
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),
            'LastName':forms.TextInput(attrs={'class':'form-control'}),
            'Course':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'State_of_origin': forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_birth':forms.TextInput(attrs={'class':'form-control'}),
            'Registration_Date':forms.TextInput(attrs={'class':'form-control'}),
            'Starting_Date': forms.TextInput(attrs={'class':'form-control'}),
            'Ending_Date':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
        }


# class Task_form(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = '__all__'
#         labels = {
#             'Name':'Full Name',
#             'Course':'Desired Course',
#             'Email':'Email',
#             'Enquiry_date': 'Date of registration',
#             'starting_date': 'Resumption date',
#             'Phone':'Phone Number'
#         }
        
#         widgets = {
#             'Name':forms.TextInput(attrs={'class':'form-control'}),  
#             'Enquiry_date':forms.DateInput(attrs={'class':'form-control'}),
#             'starting_date':forms.DateInput(attrs={'class':'form-control'}),
#             'Course':forms.TextInput(attrs={'class':'form-control'}),
#             'Email':forms.EmailInput(attrs={'class':'form-control'}),
#             'Phone':forms.TextInput(attrs={'class':'form-control'}),   
#         }
