from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Student(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronimyc = models.CharField(max_length=255)
    birth_date = models.DateField("Дата рождения")
    group =  models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)



