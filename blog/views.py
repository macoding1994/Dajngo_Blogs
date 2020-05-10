from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Tag,Post,Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Exception as e:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                category = None
            else:
                post_list = Post.objects.filter(category_id=category_id)
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