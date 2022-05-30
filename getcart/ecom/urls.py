from django.contrib import admin
from django.urls import path, include
from ecom import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.loginUser,name="login"),
    #path('logout',views.logoutuser,name="logout"),
    path('signin',views.signin,name="signin"),
    path('home',views.home,name="home"),

]
