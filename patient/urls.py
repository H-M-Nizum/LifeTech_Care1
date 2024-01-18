from django.urls import path

from . import views

urlpatterns = [
    path('register/',  views.UserRegistrationViews.as_view(), name='register'),
    path('login/',  views.CustomLoginView.as_view(), name='login'),
    path('profile/',  views.profileview, name='profile'),
    path('doctor_profile/',  views.DoctorProfileView.as_view(), name='doctor_profile'),
    path('logout/',  views.userlogoutview.as_view(), name='logout'),
]