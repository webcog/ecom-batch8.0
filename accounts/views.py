from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Your Username or Password is not Match")

    return render(request, 'accounts/login.html')



def signup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return HttpResponse("Your Password is Not Match")
        elif len(password1) < 8 and len(password2) < 8:
            return HttpResponse("Your Password Length is Smaller than 8")
        
        else:
            if User.objects.filter(email=email).exists():
                return HttpResponse("Your Email Is Already Taken")
            elif User.objects.filter(username=username).exists():
                return HttpResponse("Your Username Is Already Exist")
            else:
                my_user = User.objects.create_user(username,email,password1)
                my_user.save()
                return redirect("login")    

        # username,email,password 


    return render(request, 'accounts/signup.html')


def LogoutPage(request):
    logout(request)
    return redirect("login")



def forgot_one(request):
    return render(request, 'accounts/forgot_pass_one.html')


def forgot_two(request):
    return render(request, 'accounts/forgot_pass_two.html')


def forgot_three(request):
    return render(request, 'accounts/forgot_pass_three.html')


def forgot_four(request):
    return render(request, 'accounts/forgot_pass_four.html')