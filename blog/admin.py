from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'estado', 'fecha_publicacion']
    list_filter = ['estado', 'autor']
    raw_id_fields = ['autor']
    ordering = ['-fecha_publicacion']