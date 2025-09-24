from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', cafe_list, name='cafe_list'),
    path("register/", register, name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', menu_view, name='menu'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:item_id>/<str:action>/', update_cart, name='update_cart'),
    path('account/', views.account, name='account'),
    path('change_password/', views.change_password, name='change_password'),
    path('add/', add_dish, name='add_dish'),
    path("payment/", PaymentView.as_view(), name="payment"),
    path("payment/success/", payment_success, name="payment_success"),
]

