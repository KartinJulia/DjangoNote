from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Student


def index(request):
    return HttpResponse('two index')


def add_student(request):

    student = Student()
    student.s_name = 'Jerry'
    student.save()

    return HttpResponse("Add success")


def get_students(request):

    students = Student.objects.all()

    for student in students:
        print(student.s_name)

    context = {
        "hobby" : "play games",
        "eat" : "meat",
        "students" : students,
    }

    #return HttpResponse("student list")
    return render(request,'student_list.html',context=context)


def update_student(request):

    student = Student.objects.get(pk=2)
    student.s_name = 'Jack'
    student.save()

    return HttpResponse("updated")


def delete_student(request):
    student = Student.objects.get(pk=3)
    student.delete()

    return HttpResponse("deleted")