from django.urls import path
from .views import diskon_view, buy_voucher

app_name = 'discount'

urlpatterns = [
    path('', diskon_view, name='discount'),
    path('buy-voucher/', buy_voucher, name='buy_voucher'),
]