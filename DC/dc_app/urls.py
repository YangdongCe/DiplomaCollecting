

from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from dc_app import views

urlpatterns = [
	url(r'major/$',views.MajorList.as_view()),
	url(r'credential/$',views.CredentialList.as_view()),
	#url(r'check/',views.check,),
	#url(r'majorlist/',views.majorlist,),
	#url(r'crelist/',views.credentiallist,),
	url(r'major/(?P<pk>[0-9]+)/$', views.MajorDetail.as_view()),
	#url(r'cre/(?P<pk>[0-9]+)/$', views.CredentialDetail.as_view()),
	url(r'cre/', views.CredentialDetail.as_view()),
	url(r'majorselect/',views.MajorSelect.as_view()),
	url(r'credentialselect/',views.CredentialSelect.as_view()),
	url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
