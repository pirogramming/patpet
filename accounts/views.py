from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile, User
from my_profile.forms import CommentForm
from my_profile.models import Post, Comment
from .forms import SignupForm, ProfileForm
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers


LOGGED_IN_HOME = '/home/post_list'


def login_forbidden(function=None, redirect_field_name=None, redirect_to=LOGGED_IN_HOME):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the homepage if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=redirect_to,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@login_forbidden
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })



@login_required
def profile(request, user_profile_id):
    user = get_object_or_404(User, pk=user_profile_id)
    profile = get_object_or_404(Profile, pk=user_profile_id)
    all_profile = Profile.objects.all()
    post_list = profile.user.post_set
    post_user = get_object_or_404(get_user_model(), pk=user_profile_id)
    profile_post = post_user.post_set.all()
    comment_form = CommentForm()
    return render(request, 'accounts/profile.html', {
        'profile_user': user,
        'request_user': request.user.id,
        'real_profile_user': profile,
        'post_list': post_list,
        'profile_post_list': profile_post,
        'all_profile':all_profile,
        'comment_form': comment_form,
    })

@login_forbidden
def login(request):
    settings.LOGIN_REDIRECT_URL = '/accounts/error/'
    providers = []
    for provider in get_providers():

        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return LoginView.as_view(
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})(request)

@login_required
def follow_user(request, user_profile_id):
    #debug
    # print(request.user.profile.id)
    # print(user_profile_id)
    profile_to_follow = get_object_or_404(Profile, pk=user_profile_id)
    user_profile = request.user
    data = {}

    if int(user_profile_id) == request.user.profile.id:
        messages.warning(request, "You can not follow yourself")
    elif profile_to_follow.follows.filter(id=user_profile.id).exists():
        messages.warning(request, "You are already following this user.")
    else:
        profile_to_follow.follows.add(user_profile)
        messages.success(request, "You are now following {}".format(profile_to_follow.user))
    # print(data)
    t = user_profile.followed_by.all()
    # print(t)

    return redirect('accounts:profile', user_profile_id)



@login_required
def unfollow_user(request, user_profile_id):
    profile_to_follow = get_object_or_404(Profile, pk=user_profile_id)
    user_profile = request.user
    data = {}
    if profile_to_follow.follows.filter(id=user_profile.id).exists():
        profile_to_follow.follows.remove(user_profile)
        messages.success(request, "You are now unfollowing {}.".format(profile_to_follow.user))
    else:
        messages.warning(request, "You are not following this user")
    return redirect('accounts:profile', user_profile_id)


@login_required
def profile_redirect(request):
    return redirect('/home/post_list')

@login_required
def search(request):
    qs = User.objects.all()
    # print(qs)
    q = request.GET.get('q', '')
    # print(q)

    if q:
        profile = []
        qs = qs.filter(username__icontains=q)
        for qp in qs:

            profile.append(get_object_or_404(Profile, pk=qp.id))
        #     print(profile)
        # print(profile)
        return render(request, 'accounts/search.html', {
            'user_result': qs,
            'q': q,
            'profile_user': profile
        })
    else:
        return redirect('accounts:searchtest')


@login_required
def profile_edit(request, pk):
    post = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # post.ip = request.META['REMOTE_ADDR']
            # post.save()
            return redirect('accounts:profile', pk)
    else:
        form = ProfileForm(instance=post)
    return render(request, 'accounts/profile_edit.html', {
        'form': form,
        })

def searchtest(request):
    return render(request, 'accounts/search_test_form.html')


def recommendation(request):
    all_user = User.objects.all()  #모든 유저
    all_profile = Profile.objects.all()
    my_all_following = request.user.followed_by.all() #요청 유저 팔로잉 유저목록
    profile_user = get_object_or_404(Profile, id=request.user.id)

    profile_user.recommend.clear() #field 초기화

    common_list = [] #공통 친구 리스트
    my_following_list = [] #내 팔로잉 리스트

    for each_follow in my_all_following:  #내 팔로잉 리스트 추가
        id = int(each_follow.id)
        my_following_list.append(id)

    # print(my_following_list)

    for each_user in all_user : #모든유저 순차적
        # print(each_user)
        if each_user.id in my_following_list:  #내 팔로잉 리스트에 있으면 패스
            # if each_user.id in profile_user
            pass
        else:
            if each_user.id != request.user.id: #내와 같지 않으면 전개
                each_following = each_user.followed_by.all() #유저별 팔로잉 목록
                same_following = set(each_following).intersection(set(my_all_following)) #겹치는 팔로잉 set

                if len(same_following) != 0: #겹치는 사람이 1명 이상일때
                    common_dict = {}
                    common_dict['user'] = each_user.id
                    common_dict['intersection'] = len(same_following)
                    # print(common_dict)
                    common_list.append(common_dict) #list 안에 dict (유저,유저별 겹치는 횟수) 추가

    def sortFunc(e):        #intersection 기준 정렬
        return e['intersection']

    common_list.sort(key=sortFunc)
    common_list.reverse()


    legnth = len(common_list)

    # print('1')
    # print(common_list)

    if len(common_list) > 10:   #그결과가 10명 이상일시 5명만 표시
        for i in range(0, 4):    #10명 이하일 시 그냥 전체 표시
            # print(common_list[i]['user'])
            # print(common_list[i]['intersection'])
            profile_user.recommend.add(common_list[i]['user'])
    else:
        # print(int(len(common_list)/2))
        for i in range(0, int(len(common_list))):    #10명 이하일 시 그냥 전체 표시
            # print(common_list[i]['user'])
            # print(common_list[i]['intersection'])
            profile_user.recommend.add(common_list[i]['user'])

    common = profile_user.recommend.all()
    return render(request, 'accounts/search_test_form.html', {
        'length': legnth,
        'common': common,
        'all_profile': all_profile,
    })