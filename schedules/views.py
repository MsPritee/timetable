
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Subject, Class, Classroom, Timeslot, Timetable
from .serializers import TeacherSerializer, ClassSerializer, SubjectSerializer, ClassroomSerializer, TimeslotSerializer, TimetableSerializer
from rest_framework.response import Response #for bulk insertion
# from rest_framework.views import APIView

class BulkCreateMixin:
    """Mixin to allow bulk creation in ModelViewSet."""
    def create(self, request, *args, **kwargs):
        is_bulk = isinstance(request.data, list)  # Check if request contains a list

        if is_bulk:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ViewSet for Teacher
class TeacherViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # def create(self, request, *args, **kwargs):
    #     if isinstance(request.data, list):  # Handle bulk creation
    #         serializer = self.get_serializer(data=request.data, many=True)
    #     else:  # Handle single creation
    #         serializer = self.get_serializer(data=request.data)
        
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# ViewSet for Class
class ClassViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    # def post(self, request, *args, **kwargs):
    #     if isinstance(request.data, list):
    #         serializer = ClassSerializer(data=request.data, many=True)
    #     else:
    #         serializer = ClassSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ViewSet for Subject
class SubjectViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # def create(self, request, *args, **kwargs):
    #     if isinstance(request.data, list):
    #         serializer = self.get_serializer(data=request.data, many=True)
    #     else:
    #         serializer = self.get_serializer(data=request.data)
        
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# ViewSet for Classroom
class ClassroomViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

# ViewSet for Timeslot
class TimeslotViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Timeslot.objects.all()
    serializer_class = TimeslotSerializer

# ViewSet for Timetable
class TimetableViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    serializer_class = TimetableSerializer
    permission_classes = [IsAuthenticated]  # Ensures only logged-in users can access

    # Define queryset to avoid the basename error
    queryset = Timetable.objects.all()

    def get_queryset(self):
        # Filters timetables to show only the ones created by the logged-in user
        return Timetable.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assigns the logged-in user when creating a new timetable
        serializer.save(user=self.request.user)



# class TimetableViewSet(viewsets.ModelViewSet):
#     queryset = Timetable.objects.all()
#     serializer_class = TimetableSerializer
