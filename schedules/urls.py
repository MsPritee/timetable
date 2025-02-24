from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, SubjectViewSet, ClassViewSet, ClassroomViewSet, TimeslotViewSet, TimetableViewSet

router = DefaultRouter()
router.register(r'timetables', TimetableViewSet)
router.register(r'teachers', TeacherViewSet)  
router.register(r'subjects', SubjectViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'timeslots', TimeslotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
