from django.views.generic import ListView, DeleteView, DetailView
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def post_list(request):
    busqueda = request.GET.get('busqueda', None)  # Obtiene el término de búsqueda de la URL
    if busqueda:
        post_list = Post.objects.filter(titulo__icontains=busqueda)
    else:
        post_list = Post.objects.all()  # Obtiene todas las publicaciones del modelo Post
    return render(request, 'blog/post_list.html', context={"posts": post_list})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('blog:post_list')
            else:
                form.add_error(None, "Debes estar logueado para crear una publicación.")
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html',context={'form': form})

class PostDetailView(DetailView):
    model = Post