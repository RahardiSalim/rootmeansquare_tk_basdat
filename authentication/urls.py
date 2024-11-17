from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/pengguna/', views.register_pengguna_view, name='register_pengguna'),
    path('register/pekerja/', views.register_pekerja_view, name='register_pekerja'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.home_view, name='homepage'),  # Redirect to login for homepage
]