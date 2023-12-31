from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


""" Created a form for registration form for the users
the form will ask the user for their
first name
username
password1
password2(comfirmation of password1)"""


# we create a class for the first name
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=35, required=True,
                                 help_text='Required.')

# the registration page will have fields for the items in 'fields'
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')
