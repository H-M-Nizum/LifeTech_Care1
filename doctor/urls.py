from django.urls import path

from . import views

urlpatterns = [
    path('', views.doctorviews, name='doctor'),
    path('doctoradd/', views.RegistrationView.as_view(), name='ddoctoradd'),
    path('dg/', views.designationviews, name='dg'),
    path('designation/<slug:designation_slug>/', views.designationviews, name='designation'),
    path('sp/', views.specializationviews, name='sp'),
    path('specialization/<slug:specialization_slug>/', views.specializationviews, name='specialization'),
    path('details/<int:pk>/', views.DoctorDetailsView.as_view(), name='doctor_details_view'),

]