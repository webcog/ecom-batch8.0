from django.urls import path
from accounts.views import login_page, signup_page, LogoutPage, update_profile

from django.contrib.auth import views as auth_views 

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", signup_page, name="signup"),
    path("logout/", LogoutPage, name="logout"),
    path("profile_update/<str:username>", update_profile, name="profile_update"),



    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="accounts/password_chane.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_chane_done.html"), name="password_change_done"),
    



    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/forgot_pass_one.html"), name='password_reset'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/forgot_pass_two.html"), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/forgot_pass_three.html"), name='password_reset_confirm'),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/forgot_pass_four.html"), name='password_reset_complete'),

]


# https://docs.djangoproject.com/en/5.0/topics/auth/default/