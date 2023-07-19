from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# We have created this register Form by inheriting UserCreationForm.
# For Extending a new Field and to implement our own Form.

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
