from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('/add', Add.as_view(), name='add'),
]