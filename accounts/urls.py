from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/' , views.signup , name = "signup"),
    path('logout/' , auth_views.LogoutView.as_view() , name = 'logout'),
    path('login/' , auth_views.LoginView.as_view(template_name = 'registration/login.html') , name = 'login'),
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),name='password_change'),
    path('settings/change_password/done/' , auth_views.PasswordChangeDoneView.as_view(template_name = 'registration/change_password_done.html') , name ='password_change_done'),
    path('profile/' , views.profile , name = 'profile'),
    path('profile_edit/', views.profile_edit , name='profile_edit'),
    path('mycart/',views.my_cart,name='mycart'),
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = 'registration/rest_password.html') , name = 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/reset_password_done.html') , name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/reset_password_confirm.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/reset_password_complete.html') , name = 'password_reset_complete'),

]