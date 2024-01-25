from django import forms
from .models import DoctorModel, ReviewModel

class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorModel
        fields = '__all__'


class ReviewForm(forms.ModelForm):
       
    class Meta:
        model = ReviewModel
        fields = ['body', 'ratting']
