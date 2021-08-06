# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Accounts app
    path('users/', include('apps.accounts.urls', namespace='accounts')),

    # Main app
    path('', include('apps.main.urls', namespace='main')),

    # Admin app
    path('admin/', admin.site.urls),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
