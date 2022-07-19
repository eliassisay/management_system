from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Students

# Create your views here.
def index(request):
    return render(request,'students/index.html',{
        'students':Students.objects.all()
    })
def view_student(request,id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('view_student'))