

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","DC.settings")

import django
django.setup()
'''
def main():
	from dc_app.models import Major,Credential,Advice
	major = Major()
	credential = Credential()
	advice = Advice()
	a = '生物技术'
	b = '软件工程'
	c = '电子商务'
	l = [a,b,c]	
	f = open('h.txt')
	for line in f:
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
	from dc_app.models import Major,Credential,Advice
	
	credential = Credential()
	advice = Advice()
	from dc_app.models import Major,Credential,Advice
	major = Major.objects.all()
	credential3 = Credential.objects.all()[:3]
	credential2 = Credential.objects.all()[3:6]
	credential1 = Credential.objects.all()[6:8]
	advice = Advice()
	c = [credential1,credential2,credential3]
	i = 0
	for x in major:
		#major.m_name = x
		x.must_credential = c[i]
		i = i+1
		x.save()
if __name__ == 'main':
	main()
	print('done')








