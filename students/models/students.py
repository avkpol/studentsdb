# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Student(models.Model):
	'''Student Model'''
	class Meta(object):
		verbose_name= u"Студент"
		verbose_name_plural=u"Студенти"
	first_name= models.CharField(
		max_length=256,
		blank= False,
		verbose_name=u"Name")
	last_name = models.CharField(
		max_length=256,
		blank= False,
		verbose_name=u"Surname")
	middle_name=models.CharField(
		max_length=256,
		blank=True,
		verbose_name= u"Middle name",
		default ='')             
 	birthday=models.DateField(
		blank=False,
		verbose_name = u"date of Birth",
		null=True)
	photo= models.ImageField(
		blank=True,
		verbose_name=u"Photo",
		null=True)
	ticket=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ticket")
	student_group=models.ForeignKey('Group',
	    verbose_name=u"Група",
	    blank=False,
	    null=True,
	    on_delete=models.PROTECT)
	notes =models.TextField(
		blank=True,
		verbose_name=u"Remarks")
	
	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)

