from django.urls import path
from . import views
from .views import JobListView, JobDetailView, ApplicantListView, ApplicantDetailView, add_job, dashboard,jobs_posted_list,delete_job

urlpatterns = [
    path('job_list', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/<int:job_id>/apply/',views.apply_for_job, name='apply_for_job'),
    path('jobs/<int:job_id>/application-submitted/', views.application_submitted, name='application_submitted'),

    path('api/jobs/', JobListView.as_view(), name='job_list_api'),
    path('api/jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail_api'),
    path('api/applicants/', ApplicantListView.as_view(), name='applicant_list_api'),
    path('api/applicants/<int:pk>/', ApplicantDetailView.as_view(), name='applicant_detail_api'),

    path('add-job/', add_job, name='add_job'),
    path('applicants/',views.admin_applicant_list,name='admin_applicant_list'),
    path('applicant/<int:applicant_id>/download/',views.download_resume,name='download_resume'),
    path('applicant/<int:applicant_id>/delete/',views.delete_applicant,name='delete_applicant'),

    path('dashboard/', dashboard, name='dashboard'),
    path('jobs_posted_list/',jobs_posted_list,name='jobs_posted_list'),
    path('delete_job/<int:job_id>/',delete_job, name='delete_job'),
#recruit/anusha
    path('interview/',views.rs_process,name='interview'),
    path('rsprocess/',views.recruit_process,name='rs process'),
    path('schedule_interview/', views.schedule_interview, name='schedule_interview'),
    path('interview_list/', views.interview_list, name='interview_list'),


    path('job/shortlist/<int:interview_id>/', views.shortlist_applicant, name='shortlist_applicant'),
    path('shortlisted/', views.shortlisted_applicants, name='shortlisted_applicants'),
    path('delete/<int:id>/', views.delete_applicant, name='delete_applicant'),



]
