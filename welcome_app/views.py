from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def home(request):
    context = {
        "title": "Sample", 
        "description": "This is sample description"
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def display_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs':blogs})

def add_blog(request):
    if request.method =='POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('display_blogs')
    else:
        form = BlogForm()
    
    return render(request, 'add_blog.html', {'form': form})
