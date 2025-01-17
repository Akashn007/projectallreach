from django.urls import path
from . import views

urlpatterns = [
    path('tech/form/', views.techform_view, name='techform_view'),
    path('data/', views.technical_table_view, name='technical_table_view'),
]
