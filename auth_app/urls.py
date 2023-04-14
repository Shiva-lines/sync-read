from django.urls import path
from .views import * 

urlpatterns = [
    path('', log_in, name='log_in'),
    path('hello', log_out, name='log_out'),
    path('singup', sing_up, name='sing_up')
]