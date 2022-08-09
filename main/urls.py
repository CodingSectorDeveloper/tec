from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('redirect_to_dashboard/', views.redirect_to_dashboard, name="redirect_to_dashboard"),
]