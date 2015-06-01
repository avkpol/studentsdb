# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import datetime  
from django.views.generic import UpdateView, DeleteView ,CreateView
from django.forms import ModelForm

from ..models.students import Student
from ..models.groups import Group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..util import paginate, get_current_group

class StudentAddForm(ModelForm):
	class Meta:
		model= Student
	def __init__(self, *args, **kwargs):
		super (StudentAddForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper(self)
		
		# set form tag attributes
		self.helper.form_action = reverse('students_add', kwargs={})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		
		# set form field properties
		self.helper.help_text_inline =True
		self.helper.html5_required =True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		
		# add buttons
		self.helper.layout[-1] = FormActions(
			Submit('add_button', u'Зберегти',css_class = 'btn btn-primary'),
			Submit('cancel_button',u'Скасувати', css_class ='btn btn-link'),
			)

class StudentAddView(CreateView):
	model= Student
	template_name = 'students/students_add.html'
	form_class = StudentAddForm 
	
	def get_success_url(self):
		return u'%s?status_message= Студента успішно додано!'% reverse('home')
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=Додавання студента відмінено!'
				% reverse('home'))
		else:
			return super(StudentAddView, self).post(request, *args, **kwargs)
	
		

class StudentUpdateForm(ModelForm):
	class Meta: # determine features of model
		model = Student
	
	def __init__(self, *args, **kwargs):
		super(StudentUpdateForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper(self)
		
		# set form tag attributes
		self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		
		# set form field properties
		self.helper.help_text_inline =True
		self.helper.html5_required =True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		
		# add buttons
		self.helper.layout[-1] = FormActions(
			Submit('add_button', u'Зберегти',css_class = 'btn btn-primary'),
			Submit('cancel_button',u'Скасувати', css_class ='btn btn-link'),
			)


class StudentUpdateView(UpdateView):
	model= Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm 
	
	def get_success_url(self):
		return u'%s?status_message= Студента успішно збережено!'% reverse('home')
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=Редагування студента відмінено!'
				% reverse('home'))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)
			
class StudentDeleteView(DeleteView):
	model=Student
	template_name = 'students/students_confirm_delete.html'
	def get_success_url(self):
		return u'%s?status_message= Студента успішно видалено!'% reverse('home')
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=Відалення студента скасовано!'
				% reverse('home'))
		else:
			return super(StudentDeleteView, self).post(request, *args, **kwargs)
	
			
def students_list(request):
    # check if we need to show only one group of students
	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(student_group=current_group)
	else:
		# otherwise show all students
		students = Student.objects.all()
    # try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# paginate students
	paginator = Paginator(students, 3)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		students = paginator.page(paginator.num_pages)

	return render(request, 'students/students_list.html',
		{'students': students})
  
# def students_edit(request, sid):
#     return HttpResponse('<h1>Edit Student %s</h1>' % sid)
# 
# def students_delete(request, sid):
#     return HttpResponse('<h1>Delete Student %s</h1>' % sid)