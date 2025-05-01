from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class Bloglistview(ListView):
    model=Post
    template_name='home.html'

class Blogdetailview(DetailView):
    model=Post
    template_name='post_detail.html'

class Blogcreateview(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title', 'author', 'body']

class Blogupdateview(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title', 'body']

class Blogdeleteview(DeleteView):
    model=Post
    success_url=reverse_lazy('home')
    template_name='post_delete.html'


# Create your views here.
