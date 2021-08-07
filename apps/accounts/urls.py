# apps/accounts/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.accounts.views import UserRegistrationView

# appname
app_name = 'accounts'

urlpatterns = [
	path('register/', UserRegistrationView.as_view(), name='register')
]
