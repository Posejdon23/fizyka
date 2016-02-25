from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=100)
    email = forms.EmailField (label="Email")
    password = forms.CharField(max_length=32, min_length = 6, widget=forms.PasswordInput)
    

class LoginForm(forms.Form):
    username = forms.CharField (label="User Name")
    password = forms.CharField(max_length=32, min_length = 6, widget=forms.PasswordInput)
    