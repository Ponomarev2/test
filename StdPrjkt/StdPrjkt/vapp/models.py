from django.db import models

class Subject(models.Model):
    subjectName = models.CharField(max_length=120)
    subjectMark = models.CharField(max_length=20)


class Student(models.Model):
    nomerZachetki = models.CharField(max_length=20)
    subjectList = []

class Subject1(models.Model):
    subjectName = models.CharField(max_length=120)
    subjectMark = models.CharField(max_length=20)
    nomerZachetki = models.CharField(max_length=20)

class Profile(models.Model):
    subjectName = models.CharField(max_length=120)
    subjectMark = models.CharField(max_length=20)
    nomerZachetki = models.CharField(max_length=20)


# Create your models here.
