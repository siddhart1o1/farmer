
from django import forms
from django.template.context_processors import csrf
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Post, Farmer
from .forms import FarmerForm,PostForm
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
    if(request.method == "POST"):
        farmer_form = FarmerForm(request.POST)
        post_form = PostForm(request.POST)
        if(post_form.is_valid() and farmer_form.is_valid()):
            farmer = farmer_form.save()
            post = post_form.save(False) 
            post.farmer = farmer    
            post.save()
            return redirect(reverse("tractor:post_page"))
    else:
        farmer_form = FarmerForm()
        post_form = Post()

    args = {}
    args.update(csrf(request))
    args["farmer_form"] = farmer_form
    args["post_form"] =post_form
    return render(request,"tractor/form.html",args)


def post_detail(request,slug):
    indentified_post = get_object_or_404(Post,slug=slug)
    return render(request,"tractor/post-detail.html",{'post':indentified_post})