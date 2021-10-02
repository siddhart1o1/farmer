from django.contrib import admin

from .models import Post, Farmer
# Register your models here


class PostAdmin(admin.ModelAdmin):
    list_filter = ("farmer", "tractor_model", "implimentaion",)
    list_display = ("tractor_model", "implimentaion", "farmer",)


admin.site.register(Post, PostAdmin)
admin.site.register(Farmer)