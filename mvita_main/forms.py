from django import forms
from .models import Doctors


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = "__all__"
