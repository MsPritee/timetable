# from django.db import models
# from subjects.models import Subject
# from teachers.models import Teacher
# from classrooms.models import Classroom

# class TimeSlot(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField()

#     def __str__(self):
#         return f"{self.start_time} - {self.end_time}"

# class Timetable(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
#     timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.subject} by {self.teacher} in {self.classroom} at {self.timeslot}"


from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Class(models.Model):  # New Model for Classes
    DIVISION_CHOICES = [
        ('A', 'Div A'),
        ('B', 'Div B'),
    ]
    name = models.CharField(max_length=255, unique=True)  # Example: "TY B.Sc. CS - Sem VI"
    division = models.CharField(max_length=1, choices=DIVISION_CHOICES, default='A')

    def __str__(self):
        return f"{self.name} - {self.get_division_display()}"

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    teacher = models.ManyToManyField(Teacher)
    class_name = models.ManyToManyField(Class)  # Many-to-Many relationship
    # weekly_hours = models.IntegerField(default=2)
    theory_hours = models.IntegerField(default=2)
    practical_hours = models.IntegerField(default=2)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.room_number

class Timeslot(models.Model):   # Make sure this class is defined
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Timetable(models.Model):
    # day = models.CharField(max_length=10, choices=[
    #     ('Monday', 'Monday'),
    #     ('Tuesday', 'Tuesday'),
    #     ('Wednesday', 'Wednesday'),
    #     ('Thursday', 'Thursday'),
    #     ('Friday', 'Friday'),
    #     ('Saturday', 'Saturday'),
    # ],
    # default='Monday'  # Set a default value
    # )
    day = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="timetables")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="timetables")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="timetables")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="timetables")
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE, related_name="timetables")
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True, related_name="timetables")
    is_practical = models.BooleanField(default=False)

    class Meta:
        unique_together = ('teacher', 'timeslot', 'day', 'classroom', 'class_assigned')

    def __str__(self):
        return f"{self.day} - {self.timeslot} - {self.class_assigned} - {self.subject}"