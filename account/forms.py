from django import forms
from .models import CustomerUser
class CustomerAdd(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomerUser
        fields = ["user_name", "user_email", "user_password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("user_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")

