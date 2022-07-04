
# from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
]
