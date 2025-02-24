from django.contrib import admin
from .models import Teacher, Subject, Class, Classroom, Timeslot, Timetable

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Classroom)
admin.site.register(Timeslot)
admin.site.register(Timetable)



# @admin.register(Timetable)
# class TimetableAdmin(admin.ModelAdmin):
#     list_display = ('class_name', 'subject', 'teacher', 'day', 'time_slot', 'is_practical')
#     list_filter = ('day', 'class_name', 'teacher')