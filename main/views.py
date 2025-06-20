from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def perfil(request):
    return render(request, 'main/perfil.html')
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main:perfil')
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'main/editar_perfil.html', {'form': form})