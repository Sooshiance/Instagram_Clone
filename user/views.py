from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import User
from .forms import *


def home(request):
    return render(request, 'user/index.html')


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, phone=phone, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'خوش آمدید')
            return redirect('PROFILE')
        else:
            messages.error(request, 'مشخصات وارد شده اشتباه می باشد، دوباره تلاش کنید')
            return render(request, 'user/login.html')
    return render(request, "user/login.html")


def logoutUser(request):
    auth.logout(request)
    messages.info(request, 'به امید دیداری دوباره')
    return redirect('HOME')


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(email=email, password=password,first_name=first_name,
                                            last_name=last_name, phone=phone)
            user.set_password(password)
            return redirect('HOME')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('REGISTER')
    else:
        form = RegisterUser()
    return render(request, "user/signup.html", {'form': form})
