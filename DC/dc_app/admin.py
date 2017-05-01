from django.contrib import admin
from dc_app.models import Major,Credential
# Register your models here.
'''
内容管理系统
'''
class MajorAdmin(admin.ModelAdmin):
	list_display = ('m_name',)

class CredentialAdmin(admin.ModelAdmin):
	list_display = ('c_name','time','zhinan','search','grade','classes','question')


admin.site.register(Major,MajorAdmin)
admin.site.register(Credential,CredentialAdmin)
