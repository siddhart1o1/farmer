
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Post, Farmer
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
        form = FarmerForm(request.POST)
        if(form.is_valid()):
            
            farmer = Farmer(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],phone=form.cleaned_data['phone'],address=form.cleaned_data['address'],email_address=form.cleaned_data['email_address'])
            farmer.save()
            form.save()
            return HttpResponseRedirect("/add_post?submitted=True")
    else:
        form = FarmerForm()
        if("submitted" in request.GET):
            submitted = True
    return render(request,"tractor/form.html",{"form":form, "submitted": submitted})


def post_detail(request,slug):
    indentified_post = get_object_or_404(Post,slug=slug)
    return render(request,"tractor/post-detail.html",{'post':indentified_post})