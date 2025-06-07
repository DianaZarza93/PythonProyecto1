from django.shortcuts import render
from .models import Post

def post_list(request):
    """
    Vista para mostrar la lista de publicaciones del blog.
    """
    post_list = Post.objects.all()  # Obtiene todas las publicaciones del modelo Post
    return render(request, 'blog/post_list.html', context={"posts": post_list})
