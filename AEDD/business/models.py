from django.db import models

#meeting/anusha

class MeetingAttendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    designation = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    client = models.ForeignKey('myapp.Client', on_delete=models.CASCADE, null=True, blank=True)
    enquiry_ref_no = models.CharField(max_length=50)
    agenda = models.TextField()
    attendees = models.ManyToManyField(MeetingAttendee, related_name='meetings')
    minutes_of_meeting = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField()
    department = models.CharField(max_length=100)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Meeting: {self.enquiry_ref_no} - {self.agenda[:50]}"


class Enquiry(models.Model):
    
    enquiry = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='enquiries',null=True, blank=True)
    client = models.ForeignKey('myapp.Client', on_delete=models.CASCADE, null=True, blank=True)

    trading_services = models.TextField(blank=True, null=True)
    design_and_development = models.TextField(blank=True, null=True)
    software_design_and_dev_engineering_analysis = models.TextField(blank=True, null=True)
    manufacturing = models.TextField(blank=True, null=True)
    fabrication = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    
    # Optional: if you want a foreign key reference to the Meeting model or other relationships
    # enquiry_ref_no = models.CharField(max_length=50, unique=True) # If you want to track ref numbers
    
    def __str__(self):
        return f"Enquiry {self.id}"
    
class Graphic(models.Model):
    Graphic = models.CharField(max_length=255)
    additional = models.TextField(blank=True, null=True)
    enquiry = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='graphic_designs',null=True, blank=True)
    def __str__(self):
        return self.Graphic


class Technical_staff(models.Model):
    technical= models.CharField(max_length=255)
    enquiry = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='technical_staffing',null=True, blank=True)
    def __str__(self):
        return self.technical
    
#Quotation
class Quotation(models.Model):
    enquiry_ref = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='quotations',null=True, blank=True)
    
    quotation_no = models.CharField(max_length=100)
    quotation_date = models.DateField()
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    company_gst_no = models.CharField(max_length=50)
    gst = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    quotation_validity = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=50)
    pan_number = models.CharField(max_length=50)
    delivery_schedule = models.CharField(max_length=255)
    additional_info = models.TextField()

    def __str__(self):
        return f"Quotation {self.quotation_no}"

    class Meta:
        db_table = "quotation"  # Exact name of your manually created table


class QuotationDetails(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()
    hsn_code = models.CharField(max_length=100)
    qty = models.IntegerField()
    cost_per_qty = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.amount = self.qty * self.cost_per_qty  # Calculate amount automatically
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detail {self.description}"

    class Meta:
        db_table = "quotationdetails"  # Exact name of your manually created table


class PaymentTerm(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='payment_terms')
    term = models.CharField(max_length=255)

    def __str__(self):
        return self.term

    class Meta:
        db_table = "paymentterm"  # Exact name of your manually created table


class OtherTerm(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='other_terms')
    term = models.CharField(max_length=255)

    def __str__(self):
        return self.term

    class Meta:
        db_table = "otherterm"  # Exact name of your manually created table
#work_order/sindhu
from django.db import models

class WorkOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    scope_of_work = models.TextField()
    scope_of_work_image = models.ImageField(upload_to='scope_of_work_images/', null=True, blank=True)
    enquiry = models.ForeignKey('Meeting', on_delete=models.CASCADE, related_name='workorder', null=True, blank=True)
    client = models.ForeignKey('myapp.Client', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.po_number

