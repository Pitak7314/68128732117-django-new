from django.shortcuts import render, HttpResponse
import datetime
from .models import Student

# Create your views here.

def index(request):
    context = {
        "title":"my home page",
    }
    context["students"] = Student.objects.all().order_by("stu_id")

    context["dete"] = datetime.datetime.today()
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def student_detail(request, pk):
    context = {
        "title":"รายชื่อนักศึกษา",
    }
    context["student"] = Student.objects.get(pk=pk)
    context["dete"] = datetime.datetime.today()
    return render(request, 'student_detail.html', context)
