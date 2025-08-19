from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainers/', include('trainers.urls')),
    path('student/', include('student.urls')),
    path('', lambda request: redirect('alltrainers'), name='home'),  # Redirect root to trainer panel
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
