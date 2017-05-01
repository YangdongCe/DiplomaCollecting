from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dc_app.models import Major,Credential#,Advice


class CredentialSerializer(serializers.ModelSerializer):
	#must_major = serializers.ManyToManyField.related_name('must')
	#must_major = m.must.all()
	#advise_majbor = m.advise.all()
	#must = serializers.RelatedField(many=True,related_name='must_c',read_only=True)
	#must = serializers.RelatedField(many=True,related_name='advise_c',read_only=True)
	#must_major = Major.must_c.all()
	#advise_major = Major.advise_c.all()
	#c = Credential.objects.all()().prefetch_related('tags')
	#must = serializers.CharField(c.must_c)
	#must = serializers.ReadOnlyField(source="must_c", read_only=True)
	#advise = serializers.Serializer(source="advise_c", read_only=True, many=True)
	class Meta:
		model = Credential
		fields = ('id','c_name','time','zhinan','search','grade','classes','question','must_c','advise_c')

class MajorSerializer(serializers.ModelSerializer):
	c = Credential.objects.all()
	#majors = c.
	#credential = Major.objects.all()#.prefetch_related('must_credential')
	#must_credential = credential.must_credential.all()
	#name = CredentialSerializer(read_only=True,many=True)
	must = CredentialSerializer(source="must_credential", read_only=True, many=True)
	advise = CredentialSerializer(source="advise_credential", read_only=True, many=True)
	class Meta:
		model = Major
		fields = ('id','m_name','must','advise')#'advise_credential'
'''
class CredentialListSerializer(serializers.ModelSerializer):
	#must_major = serializers.ManyToManyField.related_name('must')
	#must_major = m.must.all()
	#advise_majbor = m.advise.all()
	#must = serializers.RelatedField(many=True,related_name='must_c',read_only=True)
	#must = serializers.RelatedField(many=True,related_name='advise_c',read_only=True)
	cc= Credential.objects.all()
	#major = c.must_c.all()
	c = CredentialSerializer(cc)
	must_major = c.must_c.all()
	advise_major = c.advise_c.all()
	class Meta:
		model = Credential
		fields = ('id','c_name','time','zhinan','search','grade','classes','question','must_major','advise_major')

'''
class RegistrationSerializer(RegisterSerializer):
	username = serializers.CharField(max_length=100)
	email = serializers.EmailField()
	password1 = serializers.CharField(write_only=True)
	password2 = serializers.CharField(write_only=True)
	major = serializers.CharField(max_length=100)
	city = serializers.CharField(max_length=100)
	school = serializers.CharField(max_length=100)
	def get_cleaned_data(self):
		return {
			'username':self.validated_data.get('username',''),
			'email':self.validated_data.get('email',''),
			'password1':self.validated_data.get('password1',''),
			'major':self.validated_data.get('major',''),
			'city':self.validated_data.get('city',''),
			'school':self.validated_data.get('school','')
		}
	def save(self,request):
		adapter = get_adapter()
		user = adapter.new_user(request)
		self.cleaned_data = self.get_cleaned_data()
		adapter.save_user(request,user,self)
		self.custom_signup(request,user)
		setup_user_email(request,user,[])
		return user