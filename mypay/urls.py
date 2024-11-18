from django.urls import path
from . import views

app_name = 'mypay'

urlpatterns = [
    path('', views.mypay_view, name='mypay'),
    path('transaction/', views.mypay_transaction_view, name='mypay_transaction'),
]