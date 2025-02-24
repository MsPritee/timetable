# Generated by Django 5.1.5 on 2025-02-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0010_rename_weekly_hours_subject_practical_hours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='is_practical',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(max_length=10),
        ),
    ]
