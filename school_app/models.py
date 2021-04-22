from django.db import models

# Create your models here.
GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6"))

class SchoolClass(models.Model):
    name = models.CharField(max_length=5)

class Subject(models.Model):
    name = models.CharField(max_length=64)

class Teacher(models.Model):
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    bio = models.TextField(null=True)

class Student(models.Model):
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    dob = models.DateField(null=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, default=1)

class StudentGrades(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.FloatField(choices=GRADES)

