from django.db import models

# Create your models here.

class Student(models.Model):
    studentId           = models.IntegerField(null=True)
    studentName         = models.CharField(null=True, max_length=20)
    studentPassword     = models.CharField(null=True, max_length=50)
    studentSubject      = models.TextField(null=True)
    studentTimetable    = models.TextField(null=True)

    def __str__(self):
        return str(self.studentId)