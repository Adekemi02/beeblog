from django.urls import path
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('register/', views.sign_up, name='signup'),
    # path('login/', views.login, name='login'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('profile/', views.profile, name='profile'),
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset-done/', auth_view.PasswordResetDoneView.as_view(
        template_name='users/password_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='users/password_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='users/password_complete.html'), name='password_reset_complete'),

]