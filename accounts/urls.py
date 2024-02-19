from django.urls import path
from accounts.views import login_page, signup_page, LogoutPage
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", signup_page, name="signup"),
    path("logout/", LogoutPage, name="logout"),
]


# https://docs.djangoproject.com/en/5.0/topics/auth/default/