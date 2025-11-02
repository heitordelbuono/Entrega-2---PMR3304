from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/novo/', views.post_create, name='post_create'),
    path('posts/<int:pk>/editar/', views.post_update, name='post_update'),
    path('posts/<int:pk>/deletar/', views.post_delete, name='post_delete'),
    path('search/', views.search_post, name='search_post'),
]