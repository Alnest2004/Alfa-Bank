from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from alfa_bank import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banking/', include('internet_banking.urls')),
    path('authorization/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
