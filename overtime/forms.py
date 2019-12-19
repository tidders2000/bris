
from django import forms
from .models import Overtime

class overtime_form(forms.ModelForm):
    class Meta:
         model = Overtime
         fields = ( 'location', 'Date','shift_start','shift_end', 'hours')
         
         
    Date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
class status_form(forms.ModelForm):
    class Meta:
        model = Overtime
        fields =( 'status',)