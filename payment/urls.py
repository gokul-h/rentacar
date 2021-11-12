
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="home"),
    path('success', views.success, name="success"),
]
