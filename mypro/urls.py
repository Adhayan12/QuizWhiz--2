from .import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('counter/',views.counter,name='counter'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('ques/', views.ques, name= 'ques'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('post/<str:pk>/', views.post, name= 'post')
    ]