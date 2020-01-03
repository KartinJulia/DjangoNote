from django.urls import path

from App import views

urlpatterns = [
    path('hello/',views.hello),
    path('index/',views.index),
    path('getstudent/',views.get_students),
    path('temp/',views.temp),
    path('home/',views.home),
]