
from django import forms
from .models import EmpDetails


class DateInput(forms.DateInput):
    input_type = 'date'


class emp_form(forms.ModelForm):
    class Meta:
        model = EmpDetails
        fields = ('__all__')
