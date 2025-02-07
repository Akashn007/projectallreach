from django.shortcuts import render, redirect
from .forms import ClientDirectoryForm
from .models import Client, ClientAddress, ClientContact, ClientEmail, ContactPersonNumber, ContactPersonEmail
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_login_myapp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='MyAppUsers').exists():
                login(request, user)
                return redirect('admin_dashboard')  # Redirect to the MyApp dashboard
            else:
                messages.error(request, 'You do not have access to MyApp.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'myapp/login.html')
@login_required(login_url='admin_login')
def ad_dashboard(request):
    return render(request, 'myapp/admin_dashboard.html')
def user_logout_myapp(request):
    logout(request)
    return redirect('admin_login')  

def dashboard(request):
    return render(request,'myapp/dashboard.html')

def admin_dashboard(request):
    return render(request,'myapp/admin_dashboard.html')

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



def client_directory(request):
    query = request.GET.get('search', '')
    if query:
        clients = Client.objects.filter(
            company_name__icontains=query
        ) | Client.objects.filter(
            department__icontains=query
        ) | Client.objects.filter(
            contact_person_name__icontains=query
        )
    else:
        clients = Client.objects.all()
    return render(request, 'myapp/client_directory.html', {'clients': clients, 'query': query})

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

                
    

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib import messages

def tech_team_dashboard(request):
    return render(request,'myapp/tech_team_dashboard.html')
# Restrict access to Tech Team only
def is_tech_team(user):
    return user.groups.filter(name='TechTeam').exists()
# Tech Team Login View
def tech_team_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if is_tech_team(user):  # Check if user is in Tech Team group
                login(request, user)
                return redirect('tech_team_dashboard')
            else:
                messages.error(request, "You are not authorized to access this page.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'myapp/tech_team_login.html')

# Tech Team Logout View
@login_required(login_url='tech_team_login')
def tech_team_logout(request):
    logout(request)
    return redirect('tech_team_login')

@login_required(login_url='tech_team_login')
@user_passes_test(is_tech_team)
def manage_credentials(request):
    if request.method == 'POST':
        if 'add_user' in request.POST:
            # Adding a new user
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            app_name = request.POST.get('app_name')  # Select which app the user belongs to
            
            if User.objects.filter(username=username).exists():
                messages.error(request, f"Username '{username}' already exists.")
            else:
                new_user = User.objects.create_user(username=username, password=password, email=email)
                group, created = Group.objects.get_or_create(name=app_name)
                new_user.groups.add(group)  # Assign user to selected app group
                messages.success(request, f"User '{username}' added successfully to {app_name}.")

        elif 'update_credentials' in request.POST:
            # Updating credentials
            username = request.POST.get('username')
            new_username = request.POST.get('new_username')
            new_password = request.POST.get('new_password')

            try:
                user = User.objects.get(username=username)
                if new_username:
                    user.username = new_username
                if new_password:
                    user.set_password(new_password)
                user.save()
                messages.success(request, f"Credentials for '{username}' updated successfully.")
            except User.DoesNotExist:
                messages.error(request, f"User '{username}' does not exist.")

        return redirect('tech_team_dashboard')

    users = User.objects.all()
    apps = Group.objects.all()  # Fetch all app groups
    return render(request, 'myapp/tech_team_dashboard.html', {'users': users, 'apps': apps})