from django import forms
from .models import Restaurant

class RestaurantAddForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'city', 'area', 'location', 'email', 'business_reg_id', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password :
          if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
         
          

         
          

         
          

         
          
