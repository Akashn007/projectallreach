from django import forms
from .models import Client

class ClientDirectoryForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'company_name',
            'company_url',
            'department',
            'contact_person_name',
            'contact_person_designation',
            'additional_info',
        ]



# client followup
from django import forms
from .models import FollowUp

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = '__all__'  # This should work if the model is defined correctly
        widgets = {
            # 'company_address': forms.Textarea(attrs={'rows': 2}),
            'follow_up_notes': forms.Textarea(attrs={'rows': 4}),
        }

#e_diary_creation
from django import forms
from .models import EDiary

class EDiaryForm(forms.ModelForm):
    class Meta:
        model = EDiary
        fields = '__all__' 
        widgets = {
            
            'meeting_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

#from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'  # This should work if the model is defined correctly
        widgets = {
            'enquiry' :forms.Textarea(attrs={'rows': 4}),
        }