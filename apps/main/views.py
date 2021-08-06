# apps/main/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import ListView 

# Locals
from apps.job.models import Job, Category 

# Create your views here.

# Homepage views
class HomeView(ListView):
	model 				= Job
	context_object_name = 'jobs'	
	paginate_by 		= 3

	# Filter job display with status published
	def get_queryset(self):
		return self.model.objects.filter(status='published')

	# Get all categories
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		categories = Category.objects.all()
		context = {
			'categories':categories		
		}
		return context

	template_name = 'main/index.html'
