from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import BlogPost

# Create your views here.
# class BlogPageView(TemplateView):
#     template_name = 'blog.html'

class BlogListView(ListView):
    template_name = 'blog.html'
    model = BlogPost
    context_object_name = 'all_blog_posts'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = revers