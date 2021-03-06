# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate, login,logout
# from django.contrib.auth.models import User,auth
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required 
# from .models import UserProfile
# from django.core.files.storage import FileSystemStorage


# def home(request):
#     return render(request,'user_profile/home.html')

# def user_signup(request):
#     if request.method=='POST':
#         user_email=request.POST['email']
#         username=request.POST['username']
#         userpass=request.POST['password']
#         try:
#             user_obj=User.objects.create(username=username,email=user_email)
#             user_obj.set_password(userpass)
#             user_obj.save()
#             user_auth=authenticate(username=username,password=userpass)
#             login(request,user_auth)
#             return redirect('home')
#         except:
#             messages.add_message(request,messages.ERROR,'can not sign up')
#             return render(request,'user_profile/signup.html')
#     return render(request,'user_profile/signup.html')



# def user_login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         userpass=request.POST['userpass']
#         try:
#             user_obj=authenticate(username=username,password=userpass)
#             login(request,user_obj)
#             request.session['username']=username
#             return redirect('home')
#         except:
#             messages.add_message(request,messages.ERROR,'can not login')
#             return render(request,'user_profile/login.html')
#     else:
#         return render(request,'user_profile/login.html')



# def user_logout(request):
#     try:
#         logout(request)
#         #messages
#     except:
#         #messages
#         return redirect('home')

# @login_required
# def user_profile(request,user_id):
#     if request.method=='POST':
#         user_obj=User.objects.get(id=user_id)
#         user_profile_obj=UserProfile.objects.get(id=user_id)
#         user_img=request.FILES['user_img']
#         fs_handle=FileSystemStorage()
#         img_name='image/user_{0}'.format(user_id)
#         if fs_handle.exists(img_name):
#             fs_handle.delete(img_name)
#         fs_handle.save(img_name,user_img)
#         user_profile_obj.profile_img=img_name
#         user_profile_obj.save()
#         user_profile_obj.refresh_from_db()
#         return render(request,'user_profile/my_profile.html',{'my_profile': user_profile_obj})
    
#     if (request.user.is_authenticated and request.user.id==user_id):
#         user_obj=User.objects.get(id=user_id)
#         user_profile=UserProfile.objects.get(id=user_id)
#         return render(request,'user_profile/my_profile.html',{'my_profile': user_profile})
        

    



from django.shortcuts import render
from .form import ImageForm
from .models import Image


def image(request):
    if request.method=="POST":  
        form=ImageForm(data=request.POST,files=request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj=form.instance 
            return render(request,"image.html",{"obj":obj}) 
    else: 
        form=ImageForm() 
        img=Image.objects.all() 
        return render(request,'image.html',{"img":img,"form":form})
  