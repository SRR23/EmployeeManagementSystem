from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.view_bio, name='profile'),
    path('update_profile/', views.update_bio, name='update_profile'),
    path('logout/', views.logout_view, name='logout'),
]
