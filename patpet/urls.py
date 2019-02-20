"""patpet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path

urlpatterns = [

    re_path(r'^$', lambda r: redirect('home:post_list'), name='root'),
    path('admin/', admin.site.urls),
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('explore/', include('explore.urls'), name='explore'),
    path('my_profile/', include(('my_profile.urls', 'my_profile'), namespace='my_profile')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)