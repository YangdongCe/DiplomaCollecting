from django.db import models




class Credential(models.Model):
	time =  models.CharField('考试时间',max_length=100)
	c_name = models.CharField('证书名字',max_length=100)
	zhinan =  models.CharField('报考指南',max_length=100)
	search =  models.CharField('成绩查询',max_length=100)
	grade =  models.CharField('分数线',max_length=100)
	classes =  models.CharField('辅导课程',max_length=100)
	question =  models.CharField('考试真题',max_length=100)
	def __str__(self):
		return self.c_name
	class Meta:
		verbose_name = '证书'
		verbose_name_plural = '证书'


class Major(models.Model):
	'''
	有两个manytomanyfield。设置related_name，表示区别。
	'''
	m_name = models.CharField('专业名称',max_length=100)
	must_credential = models.ManyToManyField(Credential,related_name='must_c',verbose_name='必考证书')#advise_credential = models.ManyToManyField(Credential)
	advise_credential = models.ManyToManyField(Credential,related_name='advise_c',verbose_name='建议证书')
	def __str__(self):
		return self.m_name

	class Meta:
		verbose_name = '专业'
		verbose_name_plural = '专业'
