from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name



class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student,through='Relationship')

    def __str__(self):
        return self.subject_name

class Relationship(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    date_registration = models.DateField()




# Create your models here.
