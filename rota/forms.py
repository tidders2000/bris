from django import forms
from .models import Rota


class rota_form(forms.ModelForm):
    class Meta:
         model = Rota
         fields = '__all__'
        