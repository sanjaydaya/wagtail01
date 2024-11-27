from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('contact/', views.contact_view, name='contact'),  # Add the contact form URL pattern
]