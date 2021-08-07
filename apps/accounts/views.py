# apps/accounts/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import CreateView 

# Locals
from apps.accounts.forms import UserRegisterForm
# Create your views here.

class UserRegistrationView(CreateView):
    template_name = 'accounts/user_register.html'
    form_class = UserRegisterForm


