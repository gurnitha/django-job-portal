# apps/main/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import ListView 

# Locals
from apps.job.models import Job 

# Create your views here.

# Homepage views
class HomeView(ListView):
	model 				= Job
	context_object_name = 'jobs'	
	paginate_by 		= 3
	template_name 		= 'main/index.html'

	def get_queryset(self):
		return self.model.objects.filter(status='published')