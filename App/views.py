from django.shortcuts import render,redirect
from django.http import JsonResponse
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
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
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    User.objects.create_user(username=username,email=email,password=password)
    Register.objects.create(email=email,username=username , password=password)

    return JsonResponse({})

def LoginPage(request):
    return render(request,'login.html')
def LoginSubmit(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    user=authenticate(request,username=email,password=password)
    m_user=Register.objects.filter(username=email)
    print(user,m_user)
    if user is not None:

        if m_user.exists():
            if m_user[0].password==password:
                login(request,user)
                return JsonResponse({'pass':True})
            else:
                return JsonResponse({'pass':False})
        else:
            return JsonResponse({'pass':False})
    else:
        return JsonResponse({'pass':False})
    
def Dashboard(request):
    return render(request, 'index.html')
    