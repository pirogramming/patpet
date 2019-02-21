from django.conf.global_settings import LOGIN_URL
from django.shortcuts import redirect
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts import views

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
    path('search/', views.search, name='search'),
    path('searchtest/', views.recommendation, name='searchtest'),
    path('<pk>/profile_edit/', views.profile_edit, name='profile_edit'),
    path('arc/', views.make_archive, name='make_archive'),
    path('<pk>/arc_edit/', views.archive_edit, name='archive_edit'),
    path('<pk>/arc_delete/', views.archive_delete, name='archive_delete'),
    path('setting/', views.main_setting, name='main_setting'),
    path('setting/arc', views.arc_setting, name='arc_setting'),
    path('all_arc/<pk>/', views.arc_all, name='arc_all'),
    path('setting/all_liked/', views.liked_all, name='liked_all'),
    path('setting/comments/', views.comment_setting, name='comment_setting'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<pk>/', views.message_detail, name='message_detail'),
    path('newmessage/', views.send_message, name='send_message'),
    # path('messages/<pk>/write/', views.send_message2, name='send_message2'),



    # path('test/', views.recommendation)

]


