
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ApplicantForm, JobForm
from rest_framework import generics, viewsets
from .models import Job, Applicant,ShortlistedApplicant,Interview
from .serializers import Jobserializer, ApplicantSerializer
from django.conf import settings
from django.http import HttpResponse, FileResponse
import os
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_login_job(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='RecruitmentUsers').exists():
                login(request, user)
                return redirect('dashboard')  # Redirect to the technical dashboard
            else:
                messages.error(request, 'You do not have access to the Technical section.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'job/login.html')

@login_required(login_url='recruitment_login')
def technical_job(request):
    return render(request, 'job/dashboard.html')
def user_logout_job(request):
    logout(request)
    return redirect('recruitment_login')

def dashboard(request):
    return render(request, 'job/dashboard.html')
def jobs_posted_list(request):
    jobs = Job.objects.all()  # Fetch all jobs from the database
    return render(request, 'job/job_posted_list.html', {'jobs': jobs})

def delete_job(request, job_id):
    if request.method == "POST":
        job = get_object_or_404(Job, id=job_id)
        job.delete()
        return redirect('job_posted_list')
    return HttpResponse("Invalid request method", status=405)

# Job Views
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Jobserializer

class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = Jobserializer

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = Jobserializer

# Applicant Views
class ApplicantListView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ApplicantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

# Function-based Views
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'job/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job/job_detail.html', {'job': job})



def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job = job
            applicant.save()
            return redirect('application_submitted', job_id=job_id)
    else:
        form = ApplicantForm()

    return render(request, 'job/apply.html', {'form': form, 'job': job})


def application_submitted(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/application_submitted.html', {'job': job})


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Replace with your job list view name
    else:
        form = JobForm()
    return render(request, 'job/add_job.html', {'form': form})

def admin_applicant_list(request):
    applicants=Applicant.objects.all()
    return render(request, 'job/admin_applicant_list.html',{'applicants':applicants})

def delete_applicant(request,applicant_id):
    applicant = get_object_or_404(Applicant,pk=applicant_id)
    applicant.delete()
    return redirect('admin_applicant_list')

def download_resume(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    resume_path = applicant.resume.path

    if os.path.exists(resume_path):
        return FileResponse(open(resume_path,'rb'), as_attachment=True, filename=os.path.basename(resume_path))
    else:
        return HttpResponse('Resume not found', status=404)


#recruit/anusha
from django.shortcuts import render
from .forms import InterviewForm
from django.http import JsonResponse

def schedule_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            print("Interview scheduled successfully")
            return JsonResponse({'message': 'Interview scheduled successfully!'}, status=201)
        else:
            # Return errors if the form is invalid
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = InterviewForm()
        applicants = Applicant.objects.all() 
    return render(request, 'job/recruit/setup interview.html', {'form': form, 'applicants': applicants})

def rs_process(request):
    return render(request,'job/recruit/R & S process.html')

def recruit_process(request):
    return render(request,'job/recruit/recruit.html')



def shortlist_applicant(request, interview_id):
    # Get the interview instance based on interview_id
    interview = get_object_or_404(Interview, id=interview_id)

    # Create a shortlisted applicant
    ShortlistedApplicant.objects.create(
        candidate=interview.candidate,
        interview=interview
    )

    # Optionally, return a success message or redirect
    return redirect('interview_list')
def shortlisted_applicants(request):
    shortlisted = ShortlistedApplicant.objects.all()
    return render(request, 'job/recruit/shortlisted.html', {'shortlisted': shortlisted})
def interview_list(request):
    interviews = Interview.objects.select_related('candidate').all()  # Fetch interviews with related candidate details
    return render(request, 'job/recruit/Recruit List.html', {'interviews': interviews})

def delete_applicant(request, id):
    interview = get_object_or_404(Interview, id=id)
    interview.delete()
    return redirect('interview_list')