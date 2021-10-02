from django import forms
from django.forms import ModelForm
from .models import Post,Farmer
from .models import Post,Farmer
from .models import Post,Farmer
from .models import Post,Farmer

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["tractor_price","implimentaion","purchase_date","tractor_company","tractor_model","description"]

class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        fields = ['first_name','last_name','phone','address','email_address']