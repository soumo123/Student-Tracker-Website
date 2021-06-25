from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    

    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("courses",views.courses,name='courses'),
    path("cases",views.cases,name='cases'),
    path("contact",views.contact,name='contact'),
    path("login",views.user_login,name='login'),
    path("logout",views.logout,name='logout'),
    path("dashboard",views.dashboard,name='dashboard'),
    # path("register",views.register),
    path('edit/<int:id>',views.editstudentdetails),
    path('update/<int:id>',views.updatestudentdetails,name='updatestudentdetails'),
    path('delete/<int:id>',views.delstudent,name='delstudent'),
    path('profile',views.profile,name='profile'),
    path('cdclogin',views.cdclogin,name='cdclogin'),
    path('profile2',views.profile2,name='profile2'),
    path('register1',views.register1,name='register1'),
    path('verification',views.verified),
    path('verify/<int:id>',views.verify,name='verify'),
    path('',views.image,name='home1'),

]
