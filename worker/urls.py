from django.urls import path
from . import views

app_name = 'worker'

urlpatterns = [
    path('', views.pekerjaan_jasa_view, name='pekerjaan_jasa'),
    path('status-pekerjaan/', views.status_pekerjaan_view, name='status_pekerjaan'),
    
]