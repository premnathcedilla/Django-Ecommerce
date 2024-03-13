
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetails

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, error_messages= { "required":"Name field should not be empty!!", "max_length":"Name must be less than 100 characters" })
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs ={'rows': 6}), error_messages={"required": "Message field cannot be empty!!!"})


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password2'].label = 'Confirm Password'
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        for field_name, field in self.fields.items():
            field.help_text = None
    
            

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

    
class LoginForm(forms.Form):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder': "Email"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': "Password"}))


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name','last_name', 'address', 'phone_number']


