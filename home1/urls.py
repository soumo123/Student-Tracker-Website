# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("",views.home,name='home'),
#     path("signup/",views.user_signup,name='sign_up'),
#     path("login/",views.user_login,name='login'),
#     path("logout",views.user_logout,name='logout'),
#     path("profile/<int:user_id>",views.user_profile,name='profile'),
 

# ]

from django.urls import path,include
from . import views

urlpatterns = [
    path('image',views.image,name='home1'),
]
