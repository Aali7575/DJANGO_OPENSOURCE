from .views import HomePage
from django.urls import path

urlpatterns = [
        path("",HomePage,name = "home")
        ]
