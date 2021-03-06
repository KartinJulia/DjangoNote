from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)

class Order(models.Model):
    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    c_name = models.CharField(max_length=18)
    c_cost = models.IntegerField(default=10)

class Company(models.Model):
    c_name = models.CharField(max_length=16)
    c_girl_num = models.IntegerField(default=10)
    c_boy_num = models.IntegerField(default=10)

