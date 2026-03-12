from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include('users.api_urls')),
    path('api/', include('projects.api_urls')),
    path('api/', include('tasks.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)