
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","DC.settings")


import django
django.setup()
'''
def main():
	from dc_app.models import Major,Credential,Advice
	major = Major()
	
	advice = Advice()
	a = '生物技术'
	b = '软件工程'
	c = '电子商务'
	l = [a,b,c]	
	f = open('h.txt',errors='ignore',encoding='utf-8')
	for line in f:
		print(line)
		credential = Credential()
		time,c_name,zhinan,search,grade,classes,question=line.split('|')
		credential.time = time
		credential.c_name = c_name
		credential.zhinan = zhinan
		credential.search = search
		credential.grade = grade
		credential.classes = classes
		credential.question = question
		credential.save()
	f.close()
'''
def main():
	a = '生物技术'
	b = '软件工程'
	c = '电子商务'
	l = [a,b,c]		
	from dc_app.models import Major,Credential
	credential1 = Credential.objects.all()[:3]
	credential2 = Credential.objects.all()[3:6]
	credential3 = Credential.objects.all()[6:8]
	c = [credential1,credential2,credential3]
	print(credential1)
	print(credential2)
	print(credential3)
	i = 0
	#major = Major.objects.all()[:1]
	#major.must_credential = credential1
	major = Major.objects.all()
	for x in major:		
		#major.m_name = x
		# = c[i]
		x.advise_credential = c[i]
		i = i+1
		print(x.advise_credential)
		x.save()

main()
print('done')








