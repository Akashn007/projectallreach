from django.urls import path
from .views import add_enquiry_form,enquiry_rfq_list,create_quotation, quotation_list,view_details,edit_quotation,delete_quotation
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('business-dev/',views.business_dashboard,name='business_dashboard'),


    #enquiry/akash
    path('enquiry_form/', add_enquiry_form, name='add_enquiry_form'),
    path('enquiry_list/', enquiry_rfq_list, name='enquiry_rfq_list'),
    # path('<int:pk>/edit/', enquiry_rfq_edit, name='enquiry_rfq_edit'),
    # path('<int:pk>/delete/', enquiry_rfq_delete, name='enquiry_rfq_delete'),
    
    #quotation/akash
    path('q_create/', create_quotation, name='create_quotation'),
    path('q_list/', quotation_list, name='quotation_list'),
    path('q_detail/<int:quotation_id>/', view_details, name='quotation_details'),
    path('q_edit/<int:quotation_id>/', edit_quotation,name='edit_quotation' ),
    path('q_delete/<int:quotation_id>/', delete_quotation,name='delete_quotation'),

    #meeting/anusha
    path('meeting_list/', views.meeting_list, name='meeting_list'),
    path('meeting_create/', views.create_meeting, name='meeting_create'),
    path('meetings/<int:meeting_id>/', views.meeting_detail, name='meeting_detail'),
    path('meetings/<int:meeting_id>/edit/', views.edit_meeting, name='meeting_edit'),
    path('meetings/<int:meeting_id>/delete/', views.delete_meeting, name='meeting_delete'),

    #work_order/sindhu
    path('', views.work_order_list, name='work_order_list'),
    path('work_order/', views.work_order_details, name='work_order_create'),  # URL for creating a new WorkOrder
    path('work_order/<int:pk>/', views.work_order_view, name='work_order_detail'),
    path('work_order/<int:pk>/edit/', views.work_order_edit, name='work_order_edit'),
    path('work_order/<int:pk>/delete/', views.work_order_delete, name='work_order_delete'),

    path('login/', views.user_login_business, name='business_login'),
    path('logout/', views.user_logout_business, name='business_logout'),

 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)