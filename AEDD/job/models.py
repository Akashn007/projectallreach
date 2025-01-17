from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Job(models.Model):
    jobid = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    experience=models.CharField(max_length=10, default=0)
    salary = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    application_deadline = models.DateField()
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.title
    
class Applicant(models.Model):
    PREFIX_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs.'),
        ('Dr.', 'Dr.'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, default='Mr.')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    college_name=models.CharField(max_length=255)
    year_of_grad = models.IntegerField()
    degree = models.CharField(max_length=100)
    stream=models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    company_name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_current_company = models.BooleanField(default=False)
    work_exp=models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    company_loc=models.CharField(max_length=255, blank=True, null=True)

    location=models.CharField(max_length=200)
    address=models.TextField()
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    resume=models.FileField(upload_to='resumes/')
    applied_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.prefix} {self.name}"
    
#recruit/anusha
class Interview(models.Model):
    candidate_name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    interview_date = models.DateField()
    interview_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate_name} - {self.position}"


class ShortlistedApplicant(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    shortlisted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant.name