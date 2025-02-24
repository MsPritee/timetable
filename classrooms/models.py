from django.db import models

class Classroom(models.Model):
    room_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.room_number
