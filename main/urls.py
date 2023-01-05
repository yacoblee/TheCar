from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name='main'),
    path('company/', company, name='company'),
]