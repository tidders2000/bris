from django import forms
from .models import Absence


class absence_form(forms.ModelForm):

    class Meta:
        model = Absence
        fields = ('user', 'absence_start', 'absence_end', 'reason',
                  'days', 'gp_consult', 'further_support')

    absence_start = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
    )
    absence_end = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y '),
        required=False

    )
