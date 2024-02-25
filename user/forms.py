from django import forms 

from .models import User



class RegisterUser(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['phone', 'password', 'email', 'first_name', 'last_name']
        labels = {
            "phone": "شماره همراه",
            "password": "گذر واژه",
            "email": "پست الکترونیکی",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
        }
        widgets = {
            "phone": forms.NumberInput(attrs={'class':'form-control my-5'}),
            "password": forms.PasswordInput(attrs={'class':'form-control my-5'}),
            "email": forms.EmailInput(attrs={'class':'form-control my-5'}),
            "first_name": forms.TextInput(attrs={'class':'form-control my-5'}),
            "last_name": forms.TextInput(attrs={'class':'form-control my-5'}),
        }
