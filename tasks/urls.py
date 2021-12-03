from django.urls import path

from .views import taskGet, taskPost

urlpatterns = [
    path('get', taskGet.as_view()),
    path('post', taskPost.as_view()),
   
]
