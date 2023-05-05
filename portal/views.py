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
    # content=request.POST.getlist('content')
    # content_image=request.FILES.getlist('content_image[]')
    content_dic=json.loads(request.POST.get('content_dic'))

  
    # print(image)
    
    Blog.objects.create(title=title,thumbnail=image)

    for i in content_dic:
        print(i)
        
        
        

        # BlogContents.create(content=content,content_image=content_image)
        # # content_image=BlogContents(image=content_image[i], content=content[i])
        # BlogContents.save()
        
        
    return JsonResponse({'status': 'Upload Done'})
