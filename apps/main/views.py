# apps/main/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# Homepage views
def home_page(request):
	return render(request, 'main/index.html')