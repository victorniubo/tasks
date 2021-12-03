from django.urls import path

from .views import taskGet, taskPost, taskDelete

urlpatterns = [
    path('post', taskPost, name='post'),
    path('get', taskGet, name='get'),
    path('delete', taskDelete, name='delete'),
   
]
