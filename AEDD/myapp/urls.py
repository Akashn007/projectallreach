from django.urls import path
from . import views
from . views import follow_up_list,follow_up_create,follow_up_delete,follow_up_edit
urlpatterns = [
    path('add-client-directory/', views.add_client_directory, name='add_client_directory'),
    path('client-directory/', views.client_directory, name='client_directory'),
    path('',views.dashboard,name='dashboard'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),

# client_followup

    path('follow_up/', follow_up_list, name='follow_up_list'),
    path('create/', follow_up_create, name='follow_up_create'),
    path('follow-up/edit/<int:pk>/',follow_up_edit, name='follow_up_edit'),
    path('follow-up/delete/<int:pk>/',follow_up_delete, name='follow_up_delete'),

#e_diary_creation
    path('diary_creation/', views.e_diary_list, name='e-diary-list'),
    path('e-create/', views.e_diary_creation, name='e-diary-create'),
    path('edit/<int:pk>/', views.edit_ediary_entry, name='edit_ediary_entry'),  # Edit view
    path('delete/<int:pk>/', views.delete_ediary_entry, name='delete_ediary_entry'),

    path('login/', views.user_login_myapp, name='login'),

    path('login/', views.user_login_myapp, name='admin_login'),
    path('logout/', views.user_logout_myapp, name='admin_logout'),

    # path('manage-credentials/', views.manage_credentials, name='manage_credentials'),

    path('tech-team/', views.manage_credentials, name='tech_team_dashboard'),
    path('tech-team/login/', views.tech_team_login, name='tech_team_login'),
    path('tech-team/logout/', views.tech_team_logout, name='tech_team_logout'),
]

