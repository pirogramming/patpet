from django.conf.global_settings import LOGIN_URL
from django.shortcuts import redirect
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts import views
from accounts.views import autocompleteModel

app_name = 'accounts'

urlpatterns = [
    path('error/', views.profile_redirect),
    path('profile/<user_profile_id>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html', authentication_form= LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=LOGIN_URL), name='logout'),
    path('follow/<user_profile_id>', views.follow_user, name='follow'),
    path('unfollow/<user_profile_id>', views.unfollow_user, name='unfollow'),
    re_path(r'^ajax_calls/search/', autocompleteModel, name='search'),

]