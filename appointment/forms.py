from django import forms

from .models import AppiontmentModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppiontmentModel
        fields = ['appointment_type', 'symptop']