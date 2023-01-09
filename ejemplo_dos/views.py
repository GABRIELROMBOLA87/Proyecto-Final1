from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from ejemplo_dos.forms import UsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

def index(request):
    return render(request, "/ejemplo_dos/index.html", {})

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post
    
class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo_dos_listar")
    fields = '__all__'
    
class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo_dos_listar")
    
class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo_dos_listar")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo_dos_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy("ejemplo_dos_listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy("ejemplo_dos_listar")


