# medicineapp/urls.py
from django.urls import path
from .views import create_medicine

urlpatterns = [
    path('create_medicine/', create_medicine, name='create_medicine'),
]
