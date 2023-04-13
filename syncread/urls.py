from django.contrib import admin
from django.urls import path, include
import account, auth_app, reader


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('auth/', include('auth_app.urls')),
    path('reader/', include('reader.urls')),
]
