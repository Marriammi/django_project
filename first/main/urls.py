from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('api/v1/hello-world-6', views.hello_world)
]