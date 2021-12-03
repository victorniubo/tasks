from django.urls import path

from . import views

urlpatterns = [
    path('', views.get, name='get'),
    path('post', views.post, name='post'),
]
