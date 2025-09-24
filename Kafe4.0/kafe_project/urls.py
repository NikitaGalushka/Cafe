from django.contrib import admin
from django.urls import path, include
from Cafe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Cafe.urls')),  # Подключаем URL-ы из приложения Cafe
    path('register/', include('Cafe.urls')),
    path('login/', include('Cafe.urls')),
    path('logout/', include('Cafe.urls')),
    path('menu/', include('Cafe.urls')),
    path('cart/', include('Cafe.urls')),
    path('add_to_cart/<int:dish_id>/', include('Cafe.urls')),
    path('remove_from_cart/<int:item_id>/', include('Cafe.urls')),
    path('update_cart/<int:item_id>/<str:action>/', include('Cafe.urls')),
    path('account/', include('Cafe.urls')),
    path('change_password/', include('Cafe.urls')),
    path('payment/', include('Cafe.urls')),
]
