
from django import forms
from .models import Leave

class leave_form(forms.ModelForm):
    class Meta:
         model = Leave
         fields = ('team', 'location', 'date_start','date_end', 'days')
         
    date_start = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
                  
    
         
    date_end = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
          