from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

from django.urls import reverse_lazy 

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    context = {}
    return render(request, 'blog/index.html', context)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

class PostListView(ListView):
    model = Post                      
    template_name = 'blog/post_list.html' 

    context_object_name = 'post_list' 

    ordering = ['-data_postagem'] 


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm                 
    template_name = 'blog/post_form.html' 

    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html' 
    success_url = reverse_lazy('post_list')         

    context_object_name = 'post'

def search_post(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'blog/search.html', context)
