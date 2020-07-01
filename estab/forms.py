from django import forms

from .models import Shifts


class shifts_form(forms.ModelForm):
    class Meta:
        model = Shifts
        fields = ('user', 'shift_start', 'shift_end', 'hours')


class shifts_form2(forms.ModelForm):
    class Meta:
        model = Shifts
        fields = ('shift_start', 'shift_end', 'hours')
