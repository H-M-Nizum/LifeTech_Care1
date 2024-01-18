from django.shortcuts import render, redirect
from . import forms
from patient.models import PatientModel
from doctor.models import DoctorModel
from appointment.models import AppiontmentModel

from .forms import RegisterForm
from django.views.generic import FormView, DetailView, CreateView
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import LoginForm
# Create your views here.

# user/ patient can registration
class UserRegistrationViews(FormView):
    template_name = 'user_regostration.html'
    form_class = forms.RegisterForm
    success_url =reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# class Userloginviews(LoginView):
#     template_name = 'user_login.html'
    
#     def get_success_url(self):
#         return reverse_lazy('home')


# All type of user can logout 
class userlogoutview(View):
    def get(self, request):
        logout(request)
        return redirect('home')


# patient profile page
def profileview(request):
    data = PatientModel.objects.filter(user=request.user)
    current_patient = request.user.patientmodel
    print(current_patient)
    apdata = AppiontmentModel.objects.filter(patient=current_patient)
    
    return render(request, 'profile.html', {'data':data, 'appointment': apdata})


# custom login for user doctor and admin
class CustomLoginView(View):
    template_name = 'user_login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Check the user's role and redirect accordingly
                if hasattr(user, 'doctormodel'):
                    return redirect('doctor_profile')
                elif hasattr(user, 'patientmodel'):
                    return redirect('profile')
                elif user.is_superuser:
                    return redirect('home')

        return render(request, self.template_name, {'form': form})

# Doctor profile page
class DoctorProfileView(View):
    template_name = 'doctor_profile.html'

    def get(self, request):
        doctor = DoctorModel.objects.get(user=request.user)
        appointments = AppiontmentModel.objects.filter(doctor=doctor)
        return render(request, self.template_name, {'doctor': doctor, 'appointments': appointments})





