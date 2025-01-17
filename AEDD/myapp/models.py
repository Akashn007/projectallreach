from django.db import models

class Client(models.Model):
    company_name = models.CharField(max_length=255)
    company_url = models.URLField(blank=True, null=True)
    department = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255)
    contact_person_designation = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class ClientAddress(models.Model):
    client = models.ForeignKey(Client, related_name='addresses', on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return f"{self.client.company_name} - Address"


class ClientContact(models.Model):
    client = models.ForeignKey(Client, related_name='company_contacts', on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.client.company_name} - Contact: {self.contact_number}"


class ClientEmail(models.Model):
    client = models.ForeignKey(Client, related_name='company_emails', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f"{self.client.company_name} - Email: {self.email}"


class ContactPersonNumber(models.Model):
    client = models.ForeignKey(Client, related_name='contact_person_numbers', on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.client.company_name} - Contact Person Number: {self.contact_number}"


class ContactPersonEmail(models.Model):
    client = models.ForeignKey(Client, related_name='contact_person_emails', on_delete=models.CASCADE)
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.client.company_name} - Contact Person Email: {self.contact_email}"


# client Followup

class FollowUp(models.Model):
    client = models.ForeignKey(Client, related_name='follow_ups', on_delete=models.CASCADE)
   
    follow_up_notes = models.TextField(default='No notes available')
   

    def __str__(self):
        return self.follow_up_notes
    

#e_diary_creation
class EDiary(models.Model):
   
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ediary_entries')
    meeting_date_time = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.meeting_date_time
    

#enquiry and requirements
class Enquiry(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='enquiries')
    enquiry = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.enquiry
    