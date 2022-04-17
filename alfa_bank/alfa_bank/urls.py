from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from alfa_bank import settings
from internet_banking.views import handler404, handler403, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banking/', include('internet_banking.urls')),
    path('authorization/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404
handler403 = handler403
handler500 = handler500
