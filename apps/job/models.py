# apps/job/models.py

# Django modules
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from config import settings

# Locals

# Create your models here.

# MODEL: Category
class Category(models.Model):
    title = models.CharField(
            max_length=100,
            blank=False,
            help_text='Category title can not be blank.')

    slug  = models.SlugField(
            editable=False,
            help_text='Slug will be added automatically based on category title.')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'  
         
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args,**kwargs)


# MODEL: Job
class Job(models.Model):

    # TODO: Define fields here

    title 	= models.CharField(
    		max_length=300,
    		blank=False,
    		help_text='Title field can not be blank.')

    slug    = models.SlugField(
            editable=False,
            help_text='This field will automatically be fullfielded.')

    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            related_name="jobs", 
            help_text='Select a category. It can not be blank.')

    company = models.CharField(
    		max_length=300,
    		blank=False,
    		help_text='Company field can not be blank.')

    # Defining type of jobs
    JOBTYPE_CHOICES = (
        ('full_time','Full time'),
        ('part_time','Part time'),
        ('freelance','Freelance'),
        ('internship','Internship'),
        ('temporary','Temporary'),
    )

    # Defining status of a job
    JOBSTATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    job_type = models.CharField(
    		max_length=20,
    		blank=False,
    		choices=JOBTYPE_CHOICES,
    		help_text='Select a type of job!')

    location = models.CharField(
    		max_length=200,
    		blank=False,
    		help_text='Example: City, Provice, Country.')

    description = models.TextField(
    		blank=False,
    		help_text='Can not be blank. Describe about the job.')

    publishing_date = models.DateTimeField(
    		default=timezone.now,
    		help_text='By default time added, but you can edit it.')
 
    employer = models.ForeignKey(
    		settings.AUTH_USER_MODEL,
    		on_delete=models.CASCADE,
    		help_text='Select an employer.')

    updated	= models.DateTimeField(auto_now=True)

    status = models.CharField(
			max_length=10,
			choices=JOBSTATUS_CHOICES,
			default='draft',
			help_text='Select the status.')

    class Meta:
        ordering = ('-publishing_date',)
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'    

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)






    