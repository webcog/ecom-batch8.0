from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def login_page(request):
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
            else:
                my_user = User.objects.create_user(username,email,password1)
                my_user.save()
                return redirect("login")    

        # username,email,password 

        


    return render(request, 'accounts/signup.html')



def forgot_one(request):
    return render(request, 'accounts/forgot_pass_one.html')


def forgot_two(request):
    return render(request, 'accounts/forgot_pass_two.html')


def forgot_three(request):
    return render(request, 'accounts/forgot_pass_three.html')


def forgot_four(request):
    return render(request, 'accounts/forgot_pass_four.html')