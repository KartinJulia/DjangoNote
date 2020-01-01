from django.urls import path

from App import views

urlpatterns = [
    path('addpersons/', views.add_persons),
    path('getpersons/', views.get_person),
    path('addperson/', views.add_person),

]