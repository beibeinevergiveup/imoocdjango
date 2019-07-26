from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['open_id']
    pass
