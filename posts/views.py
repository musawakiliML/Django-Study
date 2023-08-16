from django.shortcuts import render
from django.views.generic import ListView

from .models import Posts

# Create your views here.
class HomePageView(ListView):
    model = Posts
    template_name = 'messageboard.html'
    context_object_name = 'all_posts_list'