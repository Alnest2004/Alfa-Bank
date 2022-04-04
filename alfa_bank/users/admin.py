from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ("username",)}

admin.site.register(User, UserAdmin)