from django.utils import timezone
from schedules.models import Timetable, Subject, Teacher, Class, Classroom, Timeslot
import random

def generate_timetable():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    time_slots = list(Timeslot.objects.all().order_by('start_time'))
    classrooms = list(Classroom.objects.all())

    if not time_slots:
        print("❌ No time slots available. Please add time slots in the database.")
        return
    
    if not classrooms:
        print("❌ No classrooms available. Please add classrooms in the database.")
        return

    Timetable.objects.all().delete()  # Clear existing timetable

    for subject in Subject.objects.all():
        assigned_hours = 0
        max_hours = subject.theory_hours + subject.practical_hours
        is_practical = False

        assigned_classes = list(subject.class_name.all())  
        if not assigned_classes:
            print(f"⚠️ No classes assigned for {subject.name}, skipping...")
            continue

        class_index = 0  

        for teacher in subject.teacher.all():
            while assigned_hours < max_hours:
                day = random.choice(days)
                available_slots = time_slots.copy()

                if not available_slots:
                    print(f"⚠️ No available time slots left for {subject.name}")
                    break
                
                slot = random.choice(available_slots)  
                classroom = random.choice(classrooms)
                assigned_class = assigned_classes[class_index]  
                class_index = (class_index + 1) % len(assigned_classes)  

                # **Check for conflicts before assigning**
                conflict_exists = Timetable.objects.filter(
                    day=day,
                    timeslot=slot
                ).filter(
                    class_assigned=assigned_class  # Class already has a lecture in this slot
                ).exists() or Timetable.objects.filter(
                    day=day,
                    timeslot=slot,
                    teacher=teacher  # Teacher already has a lecture in this slot
                ).exists() or Timetable.objects.filter(
                    day=day,
                    timeslot=slot,
                    classroom=classroom  # Classroom already in use
                ).exists()

                if conflict_exists:
                    print(f"❌ Conflict detected: {assigned_class} or {teacher} already has a lecture at {slot} on {day}. Retrying...")
                    continue  # Try again with a different slot

                print(f"✅ Creating Timetable Entry - {subject} | {teacher} | {classroom} | {assigned_class} | {slot}")

                try:
                    timetable_entry = Timetable.objects.create(
                        subject=subject,
                        teacher=teacher,
                        classroom=classroom,
                        day=day,
                        timeslot=slot,
                        is_practical=is_practical,
                        class_assigned=assigned_class
                    )

                    print(f"✅ Timetable entry created for {subject.name} - {assigned_class}")

                except Exception as e:
                    print(f"❌ Error creating timetable entry for {subject.name}: {e}")

                assigned_hours += 1
                is_practical = assigned_hours >= subject.theory_hours  

    print("🎉 Timetable generated successfully without conflicts!")
