from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Group, Role


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {'students': students})

def student_page(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, "students/student_page.html", {'student': student})

def group_list(request):
    groups = Group.objects.all()
    return render(request, "students/group_list.html", {'groups': groups})

def group_page(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, "students/group_page.html", {'group': group})

def registration(request):
    groups = Group.objects.all()
    roles = Role.objects.all()
    return render(request, "students/registration.html", {'groups': groups, 'roles': roles})
# TODO: дописать форму
def reg(request):
    student = Student.objects.create(surname=,
    name=,
    patronimyc=,
    birth_date=,
    group=,
    role=)
    student.save()