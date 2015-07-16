from django.db import models
from django.contrib import admin

# Create your models here.

class Student(models.Model):
    user_number = models.CharField(max_length=18)
    password = models.CharField(max_length=20)


class StudentProfile(models.Model):
    user = models.ForeignKey(Student)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)


class AdminUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(AdminUser)
