from django.forms import ModelForm
from .models import Restaurant

class RestaurantAddForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'