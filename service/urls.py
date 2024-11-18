from django.urls import path
from . import views

urlpatterns = [
    path('subcategory/<str:subcategory_name>/user/', views.subcategory_services_user, name='subcategory_user'),
    path('subcategory/<str:subcategory_name>/worker/', views.subcategory_services_worker, name='subcategory_worker'),
    path('create-order/', views.create_order, name='create_order'),  # Route untuk create order
    path('view-orders/', views.view_orders, name='view_orders'),    # Route untuk view orders

]
