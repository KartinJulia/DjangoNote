from django.db.models import Max, Avg, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import User, Order, Customer, Company


def get_user(request):
    username = 'kartin'
    password = '123'

    users = User.objects.filter(u_name=username)
    print(users.count())

    if users.exists():
        user = users.first()
        if user.u_password == password:
            print("access userinfo successfully")
        else:
            print('wrong password')
    else:
        print('user not exist')

    return HttpResponse('Attempt successfully')


def get_users(request):

    users = User.objects.all()[2:6]

    context={
        'users':users,
    }

    return render(request,'users_list.html',context=context)


def get_order(request):

    orders = Order.objects.filter(o_time__year = 2018)
                
    for  order in orders:
        print(order.o_num)

    return HttpResponse('Get order successfully')


def get_customer(request):

    result = Customer.objects.aggregate(Avg('c_cost'))

    print(result)

    return HttpResponse("Get max cost successfully")


def get_company(request):

    companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))

    for company in companies:
        print(company.c_name)

    return HttpResponse('Get companies')