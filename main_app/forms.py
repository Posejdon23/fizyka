from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=100, help_text="", required=True)
    email = forms.EmailField (label="Email", required=True)
    password = forms.CharField(max_length=32, min_length = 6, 
            widget=forms.PasswordInput, required=True)
  

class LoginForm(forms.Form):
    username = forms.CharField (label="User Name", widget=forms.TextInput())
    password = forms.CharField(label = "Password", max_length=32, min_length = 6, widget=forms.PasswordInput())
    

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput())
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput())