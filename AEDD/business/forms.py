from django import forms
from .models import Graphic,Technical_staff

class GraphicForm(forms.ModelForm):
    class Meta:
        model = Graphic
        fields = ['Graphic', 'additional', 'enquiry']
        widgets = {
            'Graphic': forms.TextInput(attrs={'placeholder': 'Enter graphic details'}),
            'additional': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter additional information'}),
        }

       
class TechnicalStaffForm(forms.ModelForm):
    class Meta:
        model = Technical_staff
        fields = ['technical', 'enquiry']
        widgets = {
            'technical': forms.TextInput(attrs={'placeholder': 'Enter technical staffing details'}),
        }

from django import forms
from .models import Enquiry
from myapp.models import Client


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            'client',
            'trading_services', 
            'design_and_development', 
            'software_design_and_dev_engineering_analysis', 
            'manufacturing', 
            'fabrication', 
            'additional_information'
        ]
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'trading_services': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter Trading Services details'}),
            'design_and_development': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter Design & Development details'}),
            'software_design_and_dev_engineering_analysis': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter Software Design & Engineering Analysis details'}),
            'manufacturing': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter Manufacturing details'}),
            'fabrication': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter Fabrication details'}),
            'additional_information': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter additional information'}),
        }

        
#quotation
from django import forms
from .models import Quotation, QuotationDetails, PaymentTerm, OtherTerm

# Form for Quotation
class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [
            'enquiry_ref', 'quotation_no', 'quotation_date', 'company_name', 
            'company_address', 'company_gst_no', 'gst', 'total_amount',
            'quotation_validity', 'gst_number', 'pan_number', 
            'delivery_schedule', 'additional_info'
        ]

# Form for QuotationDetails (Dynamic fields will be handled in the view)
class QuotationDetailsForm(forms.ModelForm):
    class Meta:
        model = QuotationDetails
        fields = ['description', 'hsn_code', 'qty', 'cost_per_qty']

# Form for PaymentTerm
class PaymentTermForm(forms.ModelForm):
    class Meta:
        model = PaymentTerm
        fields = ['term']

# Form for OtherTerm
class OtherTermForm(forms.ModelForm):
    class Meta:
        model = OtherTerm
        fields = ['term']


#meeting/anusha
from django import forms
from .models import Meeting, MeetingAttendee

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = MeetingAttendee
        fields = ['name', 'email', 'designation', 'contact_number']

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['client','enquiry_ref_no', 'agenda', 'date_time', 'department', 'additional_information']

    # To handle multiple attendees
    attendees = forms.CharField(widget=forms.HiddenInput(), required=False)


#work_order/sindhu
from django import forms
from .models import WorkOrder

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['client','enquiry','po_number', 'date', 'scope_of_work', 'scope_of_work_image']
