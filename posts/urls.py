from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.Post.as_view(), name='post'),
]