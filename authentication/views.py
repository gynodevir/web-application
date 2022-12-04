from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def authlogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Your Credentials were wrong') 

    return render(request,'authentication/login.html')
def authregistration(request):
    if request.method == 'POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'This email already exist!!')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')


        else:
            messages.error(request,'Password and Confirm Password are not Matched')
    return render(request,'authentication/registration.html')
def forgetpassword(request):
    return render(request,'authentication/forgot.html')
def authlogout(request):
    logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('login')
# Create your views here.
