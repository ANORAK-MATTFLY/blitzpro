from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import (Post,
                    NewsLetter)

# Create your views here.

@csrf_protect
def home(request):

    context={
        'posts':Post.objects.all(),
    }

    return render(request,'blog/home.html', context)

@csrf_protect
def base(request):

    context={
        'posts':Post.objects.all(),
    }

    if request.methode == 'POST':
        email = request.POST['email']
        new_signup = Singup()
        new_signup.email = email
        new_signup.save()


    return render(request,'blog/base.html', context)


@method_decorator(login_required, name='dispatch')
class HomeListPosts(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_post']
    paginate_by = 3

class Content(DetailView):
    model = Post

class ProgrammingListView(ListView):
    model = Post
    template_name = 'blog/programming_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-date_post']

class ProgrammingContent(DetailView):
    model = Post
    template_name = 'blog/programmingposts_detail.html'


class Hi_TechListView(ListView):
    model = Post
    template_name = 'blog/hi_tech_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-date_post']

class Hi_TechContent(DetailView):
    model = Post
    template_name = 'blog/hi_tech_content.html'



def about(request):
    return render(request,'blog/about.html')