from django.urls import URLPattern,path
from . import views
urlpatterns = [
    path("",views.starting_page,name = "starting_page"),
    path("posts",views.posts,name = "post_page"),
    path("posts/<slug:slug>",views.post_detail,name="post_detail_page"),
    path("add_post",views.add_post,name = "add_post"),
]   