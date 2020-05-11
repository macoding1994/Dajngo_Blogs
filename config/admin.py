from django.contrib import admin
from .models import SideBar,Link
from DBlogs.custom_site import custim_site

@admin.register(SideBar,site=custim_site)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title','display_type','content')


    def save_model(self, request, obj, form, change):
        '''通过给obj.owner赋值，自动设置owner'''
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)

@admin.register(Link,site=custim_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title','href','status','weight')

    def save_model(self, request, obj, form, change):
        '''通过给obj.owner赋值，自动设置owner'''
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)