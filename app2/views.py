
from django.shortcuts import render,redirect
# from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import request
from .models import Blogs
from . forms import Edit_Blog
from rest_framework import viewsets
from .serializers import BlogsSerializer


# Create your views here.

def index(request):
    blog = Blogs.objects.all()
    context={'BLOGS':blog}
    return render(request,'home.html',context)

def user_register(request):
    if request.method=='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.warning(request,'Password is wrong')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'Email already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname,lastname=lname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'Done')
            return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'You are not registered yet') 
            return redirect('register')
    return render(request,'login.html')                         

def logout(request):
    auth.logout(request)
    return redirect('login')


def  post_blog(request):
    if request.method=="POST":
        title = request.POST.get('title')
        desc = request.POST.get('Description')
        blog = Blogs(title=title,dsc=desc,user_id=request.user)
        blog.save()
        messages.success(request,"Post is submitted")
        return redirect('post_blog')
    return render(request,'blog_post.html')   


def blog_detail(request,id):
    blog = Blogs.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog_detail.html',context)


def delete(request,id):
    blog = Blogs.objects.get(id=id)
    blog.delete()
    messages.success(request,'Post is deleted')
    return redirect('/')
    

def edit(request,id):
    blog = Blogs.objects.get(id=id)
    editblog = Edit_Blog(instance=blog)
    if request.method=="POST":
        form = Edit_Blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,"Post updated")
            return redirect('/')
    return render(request,'edit_blog.html',{'edit_blog':editblog})


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
