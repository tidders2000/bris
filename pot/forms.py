
from django import forms
from .models import Pot

class pot_form(forms.ModelForm):
    class Meta:
         model = Pot
         fields = ( 'location', 'Date','pot_start','pot_end', 'hours','worked')
         
         
    Date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )