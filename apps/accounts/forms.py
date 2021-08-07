# apps/accounts/forms.py

# Django modules
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Locals
from apps.accounts.models import MyUser

# UserRegisterForm forms
class UserRegisterForm(UserCreationForm):
    # is_employee and is_employer are refering to
    # MyUser model
    USERTYPES_CHOICES = [
        ('is_employee','Employee'),
        ('is_employer','Employer')]

    # User types fields
    user_types = forms.CharField(
        label="User Type",
        widget=forms.RadioSelect(choices=USERTYPES_CHOICES))

    # Define fields based-on the MyUser model
    # Password field is not included, due to Django
    # already includes it by default
    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name']

