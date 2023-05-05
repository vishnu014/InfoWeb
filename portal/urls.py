from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='index'),
    path('/addblogpage',views.AddBlogPage,name='addblogpage'),
    path('/addblog',views.AddBlog,name='addblog')
]
