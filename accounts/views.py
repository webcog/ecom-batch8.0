from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from accounts.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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
            messages.error(request, 'Your Username or Password is not Matched!')

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
            messages.error(request, 'Your Password is not Match')
        elif len(password1) < 8 and len(password2) < 8:
            messages.error(request, 'Your Password length is Smaller than 8')

        
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Your Email is Already Taken')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Your Username is Already Exist')
            else:
                my_user = User.objects.create_user(username,email,password1)
                my_user.save()
                return redirect("login")    

        # username,email,password 


    return render(request, 'accounts/signup.html')


def LogoutPage(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def update_profile(request, username):
    user = get_object_or_404(User,username=username)
    user_profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        user.first_name = request.POST.get('f_name')
        user.last_name = request.POST.get('l_name')
        user_profile.mobile =  request.POST.get('phone')
        user_profile.country =  request.POST.get('country')
        user_profile.city =  request.POST.get('city')
        user_profile.postal_code =  request.POST.get('postal')
        user_profile.address_one =  request.POST.get('address_one')
        user_profile.address_two =  request.POST.get('address_two')
        user_profile.bio =  request.POST.get('bio')
        user.save()
        user_profile.save()
        return redirect("index")
    



    return render(request, 'accounts/profile_update.html')