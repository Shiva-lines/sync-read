from django.urls import path
from .views import * 

urlpatterns = [
    path('', reader_app, name='reader'),
]