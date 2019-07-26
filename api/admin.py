from django.contrib import admin
from .models import App
import hashlib


# Register your models here.
@admin.register(App)
class AuthorizationUserAdmin(admin.ModelAdmin):
    fields = ['name', 'application', 'category', 'url', 'publish_date']
    pass

    def save_model(self, request, obj, form, change):
        src = obj.category + obj.application
        appid = hashlib.md5(src.encode('utf8')).hexdigest()  # 以16进制返回MD5字符串
        obj.appid = appid
        super().save_model(self, request, obj, form, change)
