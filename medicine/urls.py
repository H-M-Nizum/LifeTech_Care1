# medicineapp/urls.py
from django.urls import path
from .views import create_medicine, MedicineListView, MedicineUpdateView, MedicineDeleteView

urlpatterns = [
    path('create_medicine/', create_medicine, name='create_medicine'),
    path('medicines/', MedicineListView.as_view(), name='medicine_list'),
    path('edit/<int:pk>/', MedicineUpdateView.as_view(), name='medicine_edit'),
    path('delete/<int:id>/', MedicineDeleteView, name='medicine_delete'),



]
