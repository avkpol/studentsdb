# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models.studexam import Studexam

def exam_list(request):
    studexam = Studexam.objects.all()
    		
    return render(request, 'students/exam_list.html',
        {'studexam': studexam})

def studexam_add(request):
    return HttpResponse('<h1>Studexam Add Form</h1>')

def studexam_edit(request):
    return HttpResponse('<h1>Edit Studexam</h1>')

#def students_delete(request, sid):
#    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
