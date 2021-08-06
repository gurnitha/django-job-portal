# apps/main/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.main.views import home_page

# appname
app_name = 'main'

urlpatterns = [
    path('', home_page, name='home_page'),
]
