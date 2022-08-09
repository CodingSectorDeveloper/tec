from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main_admin_dashboard/', include('main_admin.urls')),
    path('branch_admin_dashboard/', include('branch_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
