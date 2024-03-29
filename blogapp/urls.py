from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('/comments/', views.comment_list, name='comment_list'),
    path('/signature/', views.signature_list, name='signature_list'),
    path('post/new/', views.post_new, name='post_new'),
]