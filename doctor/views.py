from django.shortcuts import render
from . import models
from .forms import DoctorForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# for email
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.

# user can see all doctor
def doctorviews(request):
    data = models.DoctorModel.objects.all()
    
    return render(request, 'doctor.html', {'data':data})

# user can see all designationviews
def designationviews(request, designation_slug = None):
    data = models.DoctorModel.objects.all()
    if designation_slug is not None:
        designation = models.DesignationModel.objects.get(slug = designation_slug)
        data = models.DoctorModel.objects.filter(designation = designation)
        
    designation = models.DesignationModel.objects.all()
    return render(request, 'designation.html', {'data':data, 'designation': designation})

# user can see all  specializationviews
def specializationviews(request, specialization_slug = None):
    data = models.DoctorModel.objects.all()
    if specialization_slug is not None:
        specialization = models.SpecializationModel.objects.get(slug = specialization_slug)
        data = models.DoctorModel.objects.filter(specialization = specialization)
        
    specialization = models.SpecializationModel.objects.all()
    return render(request, 'specialization.html', {'data':data, 'specialization': specialization})



# User can see doctor details
class DoctorDetailsView(DetailView):
    model = models.DoctorModel
    # pk_url_kwarg = 'id'
    template_name = 'doctor_details.html'


# i can delete it . it not need
class RegistrationView(View):
    template_name = 'doctor_regostration.html'
    form_class = DoctorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            doctor = form.save(commit=False)  
            user = doctor.user 

            # Send confirmation email
            email_subject = 'Confirm your email'
            email_body = render_to_string('confirm_email.html')

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            doctor.save()
            return HttpResponse("Check your email for confirmation.")
        
        return render(request, self.template_name, {'form': form})


# class ActivateAccountView(View):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = get_user_model().objects.get(pk=uid)

#             if user and default_token_generator.check_token(user, token):
#                 user.is_active = True
#                 user.save()
#                 return HttpResponse("Your account is now activated. You can log in.")
#             else:
#                 return HttpResponse("Activation link is invalid.")
#         except Exception as e:
#             return HttpResponse("Activation link is invalid.")



