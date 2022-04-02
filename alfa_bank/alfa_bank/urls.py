from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banking/', include('internet_banking.urls')),
    path('authorization/', include('users.urls')),
]
