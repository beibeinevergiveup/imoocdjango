from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('service/', include('api.urls')),
    path('auth/', include('authorization.urls'))
]
