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





]
