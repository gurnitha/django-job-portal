# apps/accounts/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView 

# Locals
from apps.accounts.forms import UserRegisterForm
# Create your views here.

class UserRegistrationView(SuccessMessageMixin,CreateView):
    template_name = 'accounts/user_register.html'
    form_class = UserRegisterForm
    success_url = '/'
    success_message = "Your user account has been created!"

    def form_valid(self, form):
        # Do not save user
        user = form.save(commit=False)
        # Clean data send from the form
        user_type = form.cleaned_data['user_types']

        # Check if user is employee
        if user_type == 'is_employee':
            user.is_employee = True 
        
        # Check if user is employer
        elif user_type == 'is_employer':
            user.is_employer = True

        # Save user
        user.save()

        return redirect(self.success_url)
