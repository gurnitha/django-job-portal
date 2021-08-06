# apps/job/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.job.models import Job, Category

# Register your models here.
admin.site.register(Job)
admin.site.register(Category)

