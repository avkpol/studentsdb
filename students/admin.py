# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from .models.students import Student
from .models.monthjournal import MonthJournal 
from .models.groups import Group
from .models.studexam import Studexam
from django.forms import ModelForm, ValidationError

class StudentFormAdmin(ModelForm):
	def clean_student_group(self):
		"""Check if student is leader in any group.
		 If yes, then ensure it's the same as selected group."""
	  # get group where current student is a leader
		groups= Group.objects.filter(leader = self.instance)
		if len(groups)> 0 and self.cleaned_data['student_group']!= groups[0]:
			raise ValidationError(u'Студент є старостою іншої групи', code='invalid')
		return self.cleaned_data['student_group']

class GroupFormAdmin(ModelForm):
	def clean_leader(self):
		student=Student.objects.filter(student_group= self.instance)
		if len(student)>0 and self.cleaned_data['student_group']!= groups[0]:
			raise ValidationError(u'Студента не можна обрати')
		return self.cleaned_data['student_group']
	
def copy_student(StudentAdmin, request, querryset):
	
    copy_student.short_description='Скопіювати обрані студенти'
	
	
class StudentAdmin(admin.ModelAdmin):
	list_display= ['last_name','first_name','ticket','student_group']
	list_display_links= ['last_name','first_name']
	list_editable= ['student_group']
	ordering= ['last_name']
	list_filter=['student_group']
	list_per_page=10
	search_fields=['last_name','first_name','middle_name','ticket','notes']
	actions=[copy_student]
	form= StudentFormAdmin
	def view_on_site(self, obj):
		return reverse('students_edit',kwargs ={'pk':obj.id})
	
		
	

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(Studexam)
admin.site.register (MonthJournal)

