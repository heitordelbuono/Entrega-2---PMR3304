from django.urls import path, include

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/novo/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/deletar/', views.PostDeleteView.as_view(), name='post_delete'),
    path('search/', views.search_post, name='search_post'),
    path('posts/<int:pk>/comentar', views.add_comment, name='add_comment'),
    path('categorias/', views.CategoryListView.as_view(), name='category_list'),
    path('categoria/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
]