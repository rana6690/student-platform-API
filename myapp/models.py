from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=150)
    password = models.CharField(max_length=8)
    

class Department(models.Model):
    depName = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=500, unique=True)

class Subject(models.Model):
    subName = models.CharField(max_length=150, unique=True)
    department = models.ForeignKey(Department,related_name='subject',on_delete=models.CASCADE)
    createDate = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    question = models.TextField(max_length=5000)
    sub = models.ForeignKey(Subject, related_name='ques',on_delete=models.CASCADE)
    userCreate = models.ForeignKey(User,related_name='ques', on_delete=models.CASCADE)
    dateCreate = models.DateTimeField(auto_now_add=True)
