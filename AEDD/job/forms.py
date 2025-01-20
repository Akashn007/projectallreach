from django import forms
from .models import Applicant, Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'experience','description', 'location', 'salary', 'company', 'application_deadline', 'is_active']
        widgets = {
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'prefix', 'name', 'email', 'phone_number', 'gender',
            'college_name', 'year_of_grad', 'degree', 'stream',
            'cgpa', 'company_name', 'start_date', 'end_date', 'is_current_company',
            'work_exp', 'company_loc', 'location', 'address', 'state', 'country',
            'resume','job'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

#recruit/anusha
from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['candidate', 'email', 'position', 'interview_date', 'interview_time', 'notes']
       