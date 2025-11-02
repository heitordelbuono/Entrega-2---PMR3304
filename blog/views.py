from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    context = {}
    return render(request, 'blog/index.html', context)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def post_list(request):
    posts = Post.objects.all().order_by('-data_postagem')
    contexto = {'post_list': posts} 
    return render(request, 'blog/post_list.html', contexto)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    contexto = {'post': post}
    return render(request, 'blog/post_detail.html', contexto)

def post_create(request):
    if request.method == 'POST':
        novo_titulo = request.POST.get('titulo')
        novo_conteudo = request.POST.get('conteudo')
        post = Post.objects.create(
            titulo=novo_titulo,
            conteudo=novo_conteudo
        )
        return redirect('post_list') 
    
    return render(request, 'blog/post_form.html')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.save()
        return redirect('post_detail', pk=post.pk)
    
    contexto = {'post': post}
    return render(request, 'blog/post_form.html', contexto)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    contexto = {'post': post}
    return render(request, 'blog/post_confirm_delete.html', contexto)

def search_post(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'blog/search.html', context)
