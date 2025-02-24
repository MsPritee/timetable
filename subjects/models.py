from django.db import models
from teachers.models import Teacher
from schedules.models import Class 

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="subjects", null=True, blank=True)  # Many-to-Many relationship
    weekly_hours = models.IntegerField(default=2)

    # name = models.CharField(max_length=100)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

