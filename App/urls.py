from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView, name='home'),
    # path('register',views.SignUpview,name='register'),
    path('loginpage',views.LoginPage,name='loginpage'),
    path('register_submit',views.RegisterSubmit,name="registersubmit"),
    path('login_submit',views.LoginSubmit,name="loginsubmit"),
    path('dashboard',views.Dashboard,name='dashboard'),
]
