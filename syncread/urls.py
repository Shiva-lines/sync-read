from django.contrib import admin
from django.urls import path, include
import account, auth_app, reader
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('auth_app.urls')),
    path('reader/', include('reader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
