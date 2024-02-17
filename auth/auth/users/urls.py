from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, UserView, LogoutView
urlpatterns = [
    path('register',RegisterView,as_View()),
    path('Login', LoginView.as_View()),
    path('user', UserView.as_View()),
    path('Logout', LogoutView.as_View()),
]