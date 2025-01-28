from django.urls import path
from .views import platform_view, games_view, cart_view, sign_up_by_django

urlpatterns = [
    path('', platform_view, name='platform'),
    path('games/', games_view, name='games'),
    path('cart/', cart_view, name='cart'),
    path('registration/', sign_up_by_django, name='registration'),
]
