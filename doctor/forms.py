from django import forms
from .models import DoctorModel

class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorModel
        fields = '__all__'