from django.shortcuts import render
from dc_app.serializers import MajorSerializer,CredentialSerializer
# Create your views here.
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.decorators import api_view

from dc_app.models import Credential,Major
from rest_framework import permissions
from dc_app.permissions import IsSuperOrReadOnly

error = {'status':'error'}
ok = {'status':'ok'}

'''
使用class(APIView) 和使用@api_view来装饰函数，功能差不多de。使用class，url里要使用as_view()来启动class里的函数
serializer大致功能就是把数据给序列化，使用.data就可以返回json数据，可以观察一下下面几个class每次返回数据都是这样返回的。
APIview和@api_view。。。想了想。我也不清楚这额是干嘛的了，使用这比较方便。
'''

class MajorList(APIView):
	def get(self,request):
		major = Major.objects.all()
		serializer = MajorSerializer(major,many=True)
		return Response(serializer.data)
	def post(self,request):
		#self.check_object_permissions(request, obj)
		serializer = MajorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MajorDetail(APIView):
	def get_object(self,pk):#pk代表主键
		try:
			return Major.objects.get(pk=pk)
		except Major.DoesNotExist:
			raise Http404

	def get(self,request,pk):
		major =self.get_object(pk)
		serializer = MajorSerializer(major)
		return Response(serializer.data)

class CredentialList(APIView):
	#permission_classes = (permissions.IsAdminUser,)
	def get_object(self):
		obj = get_object_or_404(self.get_queryset())
		self.check_object_permissions(self.request, obj)
		return obj
	def get(self,request):
		credential = Credential.objects.all()
		serializer = CredentialSerializer(credential,many=True)
		return Response(serializer.data)
	def post(self,request):
		#if self.check_object_permissions():
		#self.check_object_permissions(request, obj)
			#print('what fuck')
		serializer =CredentialSerializer(data=request.data)
		if serializer.is_valid():#request.data和Response基于APIView和@api_view的
			serializer.save()   #reques.data获取post，put等提交的数据
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		#else:
		#	return Response(errors)

class CredentialDetail(APIView):
	def get_object(self,pk):
		try:
			return Credential.objects.get(pk=pk)
		except Credential.DoesNotExist:
			raise Http404
	def get(self,request,pk):
		#permission_classes = (permissions.IsAdminUser,)
		c = self.get_object(pk)
		#name = request.GET['name']
		#c = Credential.objects.get(c_name=name)
		serializer = CredentialSerializer(c)
		return Response(serializer.data)

class MajorSelect(APIView):
	def get(self,request):
		name = request.query_params['name']#这个获取url参数,和request.GET['']功能一样
		try:								
			m = Major.objects.get(m_name=name)
			major = MajorSerializer(m)
			return Response(major.data)
		except:
			raise Http404
class CredentialSelect(APIView):
	def get(self,request):
		name = request.query_params['name']
		try:
			m = Credential.objects.get(c_name=name)
			credential = CredentialSerializer(m)
			return Response(credential.data)
		except:
			raise Http404


'''
	def put(self,request,pk):
		major = self.get_object(pk)
		serializer = SnippetSeralizer(major,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		major = self.get_object(pk)
		major.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
'''
def update_profile(request,user_id):
	user = User.objects.get(pk=user_id)
	user.profile.city = ''
	user.save

'''
@api_view(['GET', 'POST'])
def check(request):
	if request.method == 'GET':
		username = request.GET['username']
		user = User.objects.get(username=username)
		print(user.email)
		return Response(ok)

@api_view(['GET', 'POST'])
def tuijian(request,majorname):
	if request.method == 'GET':
		credential = Major.objects.get(m_name=majorname).prefetch_related('advise_credential')
		serializer = CredentialSerializer(credential, many=True)
		return Response(serializer.data)



@api_view(['GET'])
def majorlist(request):#获取所有专业专业
	#if request.method == 'GET':	
	user = Major.objects.all()
	serializer = MajorSerializer(user,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def credentiallist(request):
	#if request.method == 'GET':	
	user = Credential.objects.all()
	serializer = CredentialSerializer(user,many=True)
	return Response(serializer.data)

@api_view(['GET','POST'])
def must(request,majorname):
	if request.method == 'GET':
		credential = Major.objects.get(m_name=majorname).prefetch_related('must_credential')
		serializer = CredentialSerializer(credential, many=True)
		return Response(serializer.data)
	return Response(error)


def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
'''



