from django.urls import path
from . import views

urlpatterns = [
    path('tech/form/', views.techform_view, name='techform_view'),
    path('data/', views.technical_table_view, name='technical_table_view'),
    path('technical/edit/<int:form_id>/', views.edit_technical_form, name='edit_technical_form'),
    path('technical/view/<int:form_id>/', views.view_technical_form, name='view_technical_form'),
    path('technical/delete/<int:form_id>/', views.delete_technical_form, name='delete_technical_form'),
    path('login/', views.user_login_technical, name='technical_login'),
    path('logout/', views.user_logout_technical, name='technical_logout'),
]

