
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .models import *
from student01.forms import studentforms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from home1.form import ImageForm
from home1.models import Image

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def courses(request):
    return render(request,'courses.html')


def cases(request):
    return render(request,'cases.html')

def contact(request):
    return render(request,'contact.html')

def user_login(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['userid']=username
            messages.success(request,'You are sign in')
            return redirect('profile2')
    
        else:
            messages.success(request,'login unsuccessful')
            return render(request,"login.html")
    else:

        return render(request,"login.html")
        
        
def register1(request):
    if request.method=="POST":
        if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('stream') and request.POST.get('skills') and request.POST.get('experience') and request.POST.get('graduation') and request.POST.get('about') and request.POST.get('img'):
            if User.objects.filter(username=request.POST.get('fullname')).exists():
                messages.success(request, 'you have already login')
                return render(request,'login.html')
            else:
                
                saverecord = Registration()
                saverecord.fullname=request.POST.get('fullname')
                saverecord.email=request.POST.get('email')
                saverecord.mobile=request.POST.get('mobile')
                saverecord.stream=request.POST.get('stream')
                saverecord.skills=request.POST.get('skills')
                saverecord.experience=request.POST.get('experience')
                saverecord.graduation=request.POST.get('graduation')
                saverecord.about=request.POST.get('about')
                saverecord.img=request.POST.get('img')
                saverecord.save()
                user = User.objects.create_user(username=request.POST.get('fullname'),email=request.POST.get('email'),password=request.POST.get('password'))
                user.save()
                messages.success(request,'save messages successfully!!')
                return redirect('/')

    else:
        print(5)
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    del request.session
    return render(request,'index.html')

def dashboard(request):
    dashboard=Registration.objects.all()
    return render(request,'dashboard.html',{'Registration': dashboard})

def editstudentdetails(request,id):
    displaystudent = Registration.objects.get(id=id)
    return render(request,'edit.html',{"Registration":displaystudent})

def updatestudentdetails(request,id):
    updatestudent=Registration.objects.get(id=id)
    form=studentforms(request.POST, request.FILES, instance=updatestudent)
    if form.is_valid():
        print(form)
        form.save()
        messages.success(request,'Record Updated Successfully...')
        return render(request,'edit.html',{'Registration':updatestudent})
    else:
        print(form)
    

def delstudent(request,id):
    deletestudent= Registration.objects.get(id=id)
    deletestudent.delete()
    dashboard=Registration.objects.all()
    return render(request,'dashboard.html',{'Registration': dashboard})
    

def profile(request):
    data=Registration.objects.all()
    return render(request,'profile.html',{'studentdata': data})


def cdclogin(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username=='CDC_GMIT':
            if user is not None:
                login(request, user)
                request.session['userid']=username
                messages.success(request,'You are sign in')
                return redirect('profile')    
            else:
                messages.success(request,'login unsuccessful')
                return render(request,"cdclogin.html")
        else:
            messages.warning(request,'invalid username')
            return render(request,"cdclogin.html")
    else:
        return render(request,"cdclogin.html")


def profile2(request):
    name=request.session.get('userid')
    studentprofile=Registration.objects.get(fullname=name)
    # studentpic=user.objects.get(name=name)
    return render(request,'profile2.html',{'displaystudent':studentprofile})


def verified(request):
    if request.method=='POST':
        id=request.POST.get('id')
        student=Registration.objects.get(id=id)
        student.verified=request.POST.get('verified')
        student.save()
        return redirect('profile')


def verify(request,id):
    student=Registration.objects.get(id=id)
    return render(request,'verification.html',{'Registration':student})
    


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
  