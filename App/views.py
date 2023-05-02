from django.shortcuts import render,redirect
from django.http import JsonResponse
from . models import *
# Create your views here.

def indexView(request):
    return render(request,'register.html')


# def SignUpview(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login.html')
#     else:
#         form = SignUpForm()
#     return render(request, 'register.html', {'form': form})

def RegisterSubmit(request):
    email=request.POST.get("email")
    password=request.POST.get('password')
  
    Register.objects.create(email=email , password=password)

    return JsonResponse({})

def LoginPage(request):
    return render(request,'login.html')
def LoginSubmit(request):
    email=request.POST.get("email")
    password=request.POST.get('password')
    
    user=Register.objects.filter(email=email)

    if user.exists():
        if user[0].password==password:
            return JsonResponse({'pass':True})
        else:
            return JsonResponse({'pass':False})
    else:
        return JsonResponse({'pass':False})
    
def Dashboard(request):
    return render(request, 'index.html')
    