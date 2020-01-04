from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Grade, Student


def students(request, g_id):

    student_list = Student.objects.filter(s_grade_id=g_id)
    return render(request,'grade_student_list.html',context=locals())


def student(request,s_id):
    print(s_id)

    return HttpResponse("Get one student")


def grades(request):
    grade_list = Grade.objects.all()


    return render(request,'grade_list.html',context=locals())


def get_time(request,hour,minute,second):

    return HttpResponse("Time %s: %s: %s" %(second,minute,hour))


def get_date(request, day, month, year):
    return HttpResponse("Time %s: %s: %s" %(month,day,year))


def learn(request):
    return HttpResponse("helen")


def have_request(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    hobby = request.GET.get('hobby')
    hobbies = request.GET.getlist('hobby')

    print(hobbies)
    print(request.POST)
    print(request.META)
    for key in request.META:
        print(key,request.META.get(key))
    print('remote ip',request.META.get('REMOTE_ADDR'))
    return HttpResponse("Respon success")


def create_student(request):

    return render(request,'student.html')


def do_create_student(request):
    print(request.method)
    username = request.POST.get('username')
    return HttpResponse(username)