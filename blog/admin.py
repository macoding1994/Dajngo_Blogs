from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from DBlogs.custom_site import custim_site
from .models import Tag, Category, Post
from DBlogs.base_admin import BaseOwnerAdmin

# Register your models here.

@admin.register(Category,site=custim_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'is_nav', 'post_count', 'created_time')
    fields = ('name', 'status', 'is_nav')


    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag,site=custim_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')



class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义过滤器只展示当前用户分类'''
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post,site=custim_site)
class PostAdmin(BaseOwnerAdmin):
    list_display = (
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    )
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    # actions_on_bottom = True

    # 编辑页面
    # save_on_top = True

    exclude = ('owner',)

    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title','category'),
                'status',
            ),
        }),
        ('内容',{
            'fields':(
                'desc',
                'content',
            ),
        }),
        ('额外信息',{'classes':('collapse',),'fields':('tag',)})
    )


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )


