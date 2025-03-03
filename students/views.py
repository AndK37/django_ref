from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Group, Role


def index(request):
        return render(request, "students/index.html")

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
    if request.method == 'POST':
        student = Student.objects.create(
            surname=request.POST.get("s"),
            name=request.POST.get("n"),
            patronimyc=request.POST.get("p"),
            birth_date=request.POST.get("date"),
            group=Group.objects.filter(name=request.POST.get("g"))[0],
            role=Role.objects.filter(name=request.POST.get("r"))[0])
        student.save()
        return redirect('/')
    groups = Group.objects.all()
    roles = Role.objects.all()
    return render(request, "students/registration.html", {'groups': groups, 'roles': roles})

