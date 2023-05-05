from operator import itemgetter
from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json
# Create your views here.

def Home(request):
    return render(request,'dashboard.html')

def AddBlogPage(request):
    
   return render(request,'add_blog.html')


def AddBlog(request):
    title= request.POST.get('title')
    image=request.FILES.get('image')
    
    content=request.POST.getlist('content_text')
    content_image=request.FILES.getlist('content_image')
    
   
    obj=Blog.objects.create(title=title,thumbnail=image)

    for i in range(0,len(content)):
        i_content=content[i]
        i_content_image=content_image[i]        
        BlogContents.objects.create(content=i_content,content_image=i_content_image,blog_id=obj.id)
        
        
        
    return JsonResponse({'status': 'Upload Done'})
