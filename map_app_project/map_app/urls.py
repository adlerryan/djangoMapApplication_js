# map_app/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'map_app'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    
    # Add other URL patterns if needed
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)