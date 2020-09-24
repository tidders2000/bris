
from django import forms
from .models import Overtime


class DateInput(forms.DateInput):
    input_type = 'date'


class overtime_form(forms.ModelForm):
    class Meta:
        model = Overtime
        fields = ('location', 'Date', 'shift_start',
                  'shift_end', 'hours', 'ot_type', 'ot_reason')
        widgets = {
            'Date': DateInput(),
        }


class status_form(forms.ModelForm):
    class Meta:
        model = Overtime
        fields = ('status',)
