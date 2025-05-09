from django import forms
from .models import Restaurant,Menu

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

class MenuAddForm(forms.ModelForm):
      class Meta:
          model=Menu
          fields=['item_name','cuisine','price','food_pic']
          
class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurant

        fields = ['restaurant_name', 'city', 'area', 'location', 'email', 'password','business_reg_id','contact_no','s_time','e_time','min_price','max_price','logo',]
   
         
          

         
          

         
          

         
          
