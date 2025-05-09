# forms.py

from django import forms
from .models import Table_list
from django.core.exceptions import ValidationError
from django.db.models import Q

class SearchTableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    no_of_people = forms.IntegerField(min_value=1)

class TableAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.restaurant = kwargs.pop('restaurant', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Table_list
        fields = ['table_no', 'date', 'start_time', 'end_time', 'no_of_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        table_no = cleaned_data.get('table_no')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if table_no and date and start_time and end_time and self.restaurant:

         if Table_list.objects.filter(
             table_no=table_no,
             date=date,
             restaurant=self.restaurant
            ).filter(
            Q(start_time__lt=end_time) & Q(end_time__gt=start_time)
            ).exists():
            raise ValidationError("This table already has a reservation that overlaps with the selected time.")

        return cleaned_data
