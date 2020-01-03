from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from App.models import Student


def hello(request):
    return HttpResponse("hello")


def index(request):

    temp = loader.get_template('index.html')

    content = temp.render()



    return HttpResponse(content)

def get_students(request):

    students = Student.objects.all()

    student_dict = {
        'hobby':'coding',
        'time': "5",
    }

    code = """
    <h2>Sleep</h2>
    <script>
    alert("Attacked");
    var lis = document.getElementsByTagName("li");

for (var i=0; i< lis.length; i++){
    var li = lis[i];
    li.innerHTML="fuck you"
}
    </script>
    """

    data = {
        "students": students,
        'student_dict': student_dict,
        "content": 5,
        "code": code,
    }

    return render(request,"student_list.html", context=data)


def temp(request):

    return render(request,'home.html',context={"title":"home"})


def home(request):
    return render(request,"home_mine.html")