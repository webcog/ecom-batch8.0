from django.urls import path
from accounts.views import login_page, signup_page, forgot_one, forgot_two, forgot_three, forgot_four
urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", signup_page, name="signup"),
    path("forgot_password/", forgot_one, name="for_one"),
    path("forgot_password_two/", forgot_two, name="for_two"),
    path("forgot_password_three/", forgot_three, name="for_three"),
    path("forgot_password_four/", forgot_four, name="for_four"),
]
