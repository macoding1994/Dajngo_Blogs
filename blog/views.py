from django.shortcuts import render
from django.http import HttpResponse


def post_list(request, category_id=None, tag_id=None):
    content = 'post_list  category_id:{}  tag_id:{}'.format(category_id, tag_id)
    return HttpResponse(content)


def links(request):
    return HttpResponse('links')


def detall(request, post_id=None):
    return HttpResponse('detall {}'.format(post_id))
