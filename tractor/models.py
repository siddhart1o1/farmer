from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.signals import pre_save
# Create your models here.
from .utils import unique_slug_generator

class Farmer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone =models.CharField(max_length=10,unique=True)
    address = models.TextField(max_length=200)
    email_address = models.EmailField(unique=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    tractor_price = models.IntegerField(max_length=150)
    implimentaion = models.CharField(max_length=50)
    purchase_date = models.DateField(auto_now=False)
    slug = models.SlugField(unique=True, db_index=True, null=True,blank=True)
    tractor_company = models.CharField(max_length=50)
    tractor_model = models.CharField(max_length=50)
    description = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now_add =True)
    farmer = models.ForeignKey(
        Farmer, on_delete=models.SET_NULL, null=True, related_name="posts")

    def __str__(self):
        return self.implimentaion

def slug_generator(sender, instance, *args ,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender =Post)