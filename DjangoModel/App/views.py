import random

from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):

    for i in range (15):
        person = Person()
        val=random.randrange(100)
        person.p_name = 'Tom%d' % val
        person.p_age = val
        person.p_sex = val % 2
        person.save()

    return HttpResponse('batch people created')


def get_person(request):

    persons = Person.objects.filter(p_age__gt=18)
    context = {
        'persons' : persons
    }

    return render(request, 'person_list.html', context=context)


def add_person(request):
    person = Person.create('Jack')
    # person = Person.objects.create(p_name='lucky',p_age=15,p_sex=True)
    person.save()
    return HttpResponse("created lucky")

