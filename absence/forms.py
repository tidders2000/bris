from django import forms
from .models import Absence


class DateInput(forms.DateInput):
    input_type = 'date'


class absence_form(forms.ModelForm):

    class Meta:
        model = Absence
        fields = ('user', 'absence_start', 'absence_end', 'reason',
                  'days', 'gp_consult', 'further_support')

        widgets = {
            'absence_start': DateInput(), 'absence_end': DateInput()
        }
