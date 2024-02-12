from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request, 'accounts/login.html')



def signup_page(request):
    return render(request, 'accounts/signup.html')



def forgot_one(request):
    return render(request, 'accounts/forgot_pass_one.html')


def forgot_two(request):
    return render(request, 'accounts/forgot_pass_two.html')


def forgot_three(request):
    return render(request, 'accounts/forgot_pass_three.html')


def forgot_four(request):
    return render(request, 'accounts/forgot_pass_four.html')