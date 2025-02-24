from rest_framework import serializers
from .models import Teacher, Subject, Classroom, Timeslot, Timetable, Class

# Bulk Serializer
class BulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        return self.child.Meta.model.objects.bulk_create([self.child.Meta.model(**item) for item in validated_data])

# Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer  # Enable bulk creation

# Class Serializer
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']
        list_serializer_class = BulkCreateListSerializer  # Enable bulk creation

# Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer


    # def create(self, validated_data):
    #     if isinstance(validated_data, list):  # Bulk insert
    #         subjects = []
    #         for item in validated_data:
    #             obj, created = Subject.objects.get_or_create(**item) 
    #             subjects.append(obj)  # FIXED: Append obj instead of undefined variable
    #         return subjects
    #     return super().create(validated_data)

# Classroom Serializer
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer


# Timeslot Serializer
class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer


# Timetable Serializer
class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
        list_serializer_class = BulkCreateListSerializer


    def validate(self, data):
        teacher = data.get('teacher')
        classroom = data.get('classroom')
        timeslot = data.get('timeslot')
        subject = data.get('subject')

        # Check if the teacher is already assigned at the same time
        if Timetable.objects.filter(teacher=teacher, timeslot=timeslot).exists():
            raise serializers.ValidationError("This teacher is already assigned to another class at this time.")

        # Check if the classroom is already occupied at the same time
        if Timetable.objects.filter(classroom=classroom, timeslot=timeslot).exists():
            raise serializers.ValidationError("This classroom is already occupied at this time.")

        # Check weekly hours limit for the subject (Ensure 'weekly_hours' exists in Subject model)
        if hasattr(subject, 'weekly_hours'):  # FIXED: Check if the field exists before using it
            assigned_hours = Timetable.objects.filter(subject=subject).count()
            if assigned_hours >= subject.weekly_hours:
                raise serializers.ValidationError(f"{subject.name} has reached its weekly schedule limit.")
        
        return data
