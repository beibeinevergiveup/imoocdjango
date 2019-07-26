from django.urls import path
from .views import weather, menu, image, services

urlpatterns = (
    # path('', weather.helloworld)
    path('weather', weather.weatherView.as_view()),
    path('menu', menu.get_menu),
    # path('image', image.image),
    path('imagetext', image.image_text),
    path('image', image.ImageView.as_view()),
    path('image/list', image.ImageListView.as_view()),
    path('stock', services.stock),
    path('constellation', services.constellation),
    path('joke', services.joke)

)
