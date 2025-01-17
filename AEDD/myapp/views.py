from django.shortcuts import render, redirect
from .forms import ClientDirectoryForm
from .models import Client, ClientAddress, ClientContact, ClientEmail, ContactPersonNumber, ContactPersonEmail

def add_client_directory(request):
    if request.method == 'POST':
        form = ClientDirectoryForm(request.POST)
        if form.is_valid():
            client = form.save()

            # Process additional fields
            addresses = request.POST.getlist('company_address[]')
            for address in addresses:
                ClientAddress.objects.create(client=client, address=address)

            contact_numbers = request.POST.getlist('company_contact[]')
            for contact_number in contact_numbers:
                ClientContact.objects.create(client=client, contact_number=contact_number)

            emails = request.POST.getlist('company_email[]')
            for email in emails:
                ClientEmail.objects.create(client=client, email=email)

            contact_person_numbers = request.POST.getlist('contact_number[]')
            for contact_number in contact_person_numbers:
                ContactPersonNumber.objects.create(client=client, contact_number=contact_number)

            contact_person_emails = request.POST.getlist('contact_email[]')
            for email in contact_person_emails:
                ContactPersonEmail.objects.create(client=client, contact_email=email)

            return redirect('client_directory')
    else:
        form = ClientDirectoryForm()

    return render(request, 'myapp/add_cdc.html', {'form': form})


def client_directory(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_directory.html', {'clients': clients })

def dashboard(request):
    return render(request,'myapp/dashboard.html')

def admin_dashboard(request):
    return render(request,'myapp/admin_dashboard.html')


# client_followup
from django.shortcuts import render, redirect,get_object_or_404
from .models import FollowUp
from .forms import FollowUpForm


def follow_up_list(request):
    follow_ups = FollowUp.objects.all()
    clients = Client.objects.all()
    return render(request, 'myapp/client followup.html', {'clients': clients, 'follow_ups': follow_ups})

def follow_up_create(request):
    if request.method == 'POST':
        form = FollowUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('follow_up_list')
    else:
        form = FollowUpForm()
    return render(request, 'myapp/add_follow.html', {'form': form}) 

def deleteItem(request,id):
    item = item.objects.get(id=id)
    item.delete()
    return redirect('follow_up_list')


def follow_up_edit(request, pk):
    follow_up = get_object_or_404(FollowUp, pk=pk)
    if request.method == "POST":
        form = FollowUpForm(request.POST, instance=follow_up)
        if form.is_valid():
            form.save()
            return redirect('follow_up_list')  # Redirect to the list view
    else:
        form = FollowUpForm(instance=follow_up)
    return render(request, 'myapp/follow_up_edit.html', {'form': form})

def follow_up_delete(request, pk):
    follow_up = get_object_or_404(FollowUp, pk=pk)
    if request.method == "POST":
        follow_up.delete()
        return redirect('follow_up_list')  # Redirect to the list view
    return render(request, 'myapp/follow_up_confirm_delete.html', {'follow_up': follow_up})

#e_diary_creation

from .models import EDiary
from .forms import EDiaryForm
from rest_framework import viewsets
from .serializers import EDiarySerializer

# Display List of Follow-Ups
def e_diary_list(request):
    follow_ups = EDiary.objects.all()
    clients = Client.objects.all()
    return render(request, 'myapp/E_Dairy_Creation.html', {'clients': clients,'follow_ups': follow_ups})

def e_diary_creation(request):
    if request.method == 'POST':
        form = EDiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e-diary-list')
        else:
            print("Form errors:", form.errors)  # Debugging output
            return render(request, 'myapp/add_meeting.html', {'form': form, 'errors': form.errors, 'clients': Client.objects.all()})
    else:
        form = EDiaryForm()
    return render(request, 'myapp/add_meeting.html', {'form': form, 'clients': Client.objects.all()})
def edit_ediary_entry(request, pk):
    entry = get_object_or_404(EDiary, pk=pk)
    if request.method == "POST":
        form = EDiaryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('e-diary-list')  # Ensure URL name matches `urls.py`
    else:
        form = EDiaryForm(instance=entry)
    return render(request, 'myapp/edit.html', {'form': form, 'entry': entry})

# Delete an E-Diary Entry
def delete_ediary_entry(request, pk):
    entry = get_object_or_404(EDiary, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('e-diary-list')  # Ensure URL name matches `urls.py`
    return render(request, 'myapp/delete.html', {'entry': entry})

from .models import Enquiry, Client
from .forms import EnquiryForm
from django.shortcuts import render, redirect, get_object_or_404

# Display List of Enquiries
def enquiry_list(request):
    enquiries = Enquiry.objects.all()
    clients = Client.objects.all()
    return render(request, 'myapp/enquiry.html', {'clients': clients, 'enquiries': enquiries})

# Create a New Enquiry
def enquiry_creation(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry_list')  # Ensure 'enquiry-list' matches your URLs
        else:
            print("Form errors:", form.errors)  # Debugging output
            return render(request, 'add_enquiry.html', {'form': form, 'errors': form.errors, 'clients': Client.objects.all()})
    else:
        form = EnquiryForm()  # Correct form class
    return render(request, 'myapp/add_enquiry.html', {'form': form, 'clients': Client.objects.all()})

# Edit an Enquiry
def enquiry_edit(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)  # Correct naming
    if request.method == "POST":
        form = EnquiryForm(request.POST, instance=enquiry)
        if form.is_valid():
            form.save()
            return redirect('enquiry_list')  # Ensure URL name matches `urls.py`
    else:
        form = EnquiryForm(instance=enquiry)  # Correct form class
    return render(request, 'myapp/enquiry_edit.html', {'form': form, 'enquiry': enquiry})

# Delete an Enquiry
def enquiry_delete(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)  # Correct naming
    if request.method == "POST":
        enquiry.delete()
        return redirect('enquiry_list')  # Ensure URL name matches `urls.py`
    return render(request, 'myapp/enquiry_delete.html', {'enquiry': enquiry})

                
    


