from django.contrib import admin
from comment.models import Comment
from DBlogs.custom_site import custim_site

@admin.register(Comment,site=custim_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
