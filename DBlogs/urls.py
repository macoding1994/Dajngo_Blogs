"""DBlogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .custom_site import custim_site
from blog import views as blogviews

urlpatterns = [
    url(r'^$',blogviews.post_list,name='index'),
    url(r'^category/(?P<category_id>\d+)/$',blogviews.post_list,name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$',blogviews.post_list,name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$',blogviews.detall,name='post-detail'),
    url(r'^links$',blogviews.links,name='links'),
    path('admin/', custim_site.urls,name='admin'),
    path('super_admin/', admin.site.urls,name='super-admin'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
