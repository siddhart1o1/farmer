
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import FarmerForm,PostForm,Post
from .forms import FarmerForm
# Create your views here.
from django.http import HttpResponseRedirect 
# Create your views here.
def starting_page(request):
    return render(request,"tractor/index.html")

def posts(request):
    qs = Post.objects.all()  
    context = {"posts":qs}
    return render(request,"tractor/all-post.html",context)
    
def add_post(request):
    submitted = False
    if(request.method == "POST"):
        form1 = FarmerForm(request.POST,prefix="form1")
        form2 = PostForm(request.POST,prefix="form2")
        
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect("/add_post?submitted=True")
    else:
        form1 = FarmerForm(prefix="form1")
        form2 = PostForm(prefix="form2")
        if("submitted" in request.GET):
            submitted = True
    return render(request,"tractor/form.html",{"form1":form1,"form2":form2, "submitted": submitted})

def post_detail(request,slug):
    indentified_post = get_object_or_404(Post,slug=slug)
    return render(request,"tractor/post-detail.html",{'post':indentified_post})