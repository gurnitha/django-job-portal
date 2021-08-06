# apps/accounts/admin.py

# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Locals
from apps.accounts.models import MyUser

# Register your models here.

class MyUserAdmin(UserAdmin):
    
    # model = MyUser # <-- this can be disable
    
    list_display = ('email','first_name',
                    'last_name','is_employee',
                    'is_employer', 'is_admin')
    list_filter = ('email','first_name','last_name',
                    'is_employee','is_employer')
    search_fields =  ('email','first_name','last_name')
    ordering = ('email','first_name')
    readonly_fields = ['date_joined']

    # Add users
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','first_name',
                      'last_name','password1',
                      'password2','is_employee',
                      'is_employer','is_active')
        }),
    )

    # Edit users
    fieldsets = (
        (None,{'fields':('email','first_name',
                         'last_name','password')}),
        ('Permissions',{'fields':('is_active','is_admin',
                         'is_employee','is_employer')})
    )


admin.site.register(MyUser, MyUserAdmin)