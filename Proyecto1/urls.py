from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Main app URL configuration
    path('blog/', include('blog.urls')),  # Blog app URL configuration
]
