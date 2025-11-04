from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    nome=models.CharField(max_length=100)
    descricao=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural="Categories"
        
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField() 
    data_postagem = models.DateTimeField(auto_now_add=True) 
    categories=models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    autor=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    texto=models.TextField()
    data_postagem=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_postagem']

    def __str__(self):
        return f"Comentário de {self.autor} em '{self.titulo}'"

