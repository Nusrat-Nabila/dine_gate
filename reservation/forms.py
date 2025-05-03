from django import forms
from .models import Table_list

class SearchTableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    no_of_people = forms.IntegerField(min_value=1)

class TableAddForm(forms.ModelForm):
      class Meta:
          model=Table_list
          fields=['table_no','date','start_time','end_time','no_of_people']
          widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            }