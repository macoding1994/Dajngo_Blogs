from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Tag,Post,Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        post_list , tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_postlist()

    context = {
        'category':category,
        'tag':tag,
        'post_list':post_list,
    }
    # N + 1 测试demo
    # post_list = Post.objects.all().select_related('owner','category')
    # for post in post_list:
    #     print(post.id)
    return render(request,'list.html',context=context)

def links(request):
    return HttpResponse('links')


def detall(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Exception as e:
        post = None
    return render(request,'detall.html',context={'post':post})