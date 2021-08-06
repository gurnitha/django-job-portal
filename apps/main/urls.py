# apps/main/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.main.views import HomeView

# appname
app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
]
