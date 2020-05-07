from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'blogs'
    site_title = '管理后台'
    index_title = '首页'

custim_site = CustomSite(name='cus_admin')