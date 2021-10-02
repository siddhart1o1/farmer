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

class FarmerForm(PostForm):
    #declare the field from the Farmer model here.
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone =forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)
    email_address = forms.EmailField()
    class Meta(PostForm.Meta):
        fields = ['first_name','last_name','phone','address','email_address'] + PostForm.Meta.fields