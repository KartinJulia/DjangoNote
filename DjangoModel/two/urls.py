from django.urls import path

from two import views

urlpatterns = [
    path('getuser/',views.get_user),
    path('getusers/',views.get_users),
    path('getorder/',views.get_order),
    path('getcustomer/',views.get_customer),
    path('getcompany/',views.get_company),
]