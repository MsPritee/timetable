# Generated by Django 5.1.5 on 2025-02-10 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_alter_timetable_unique_together_class_division_and_more'),
        ('subjects', '0002_subject_class_name'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='weekly_hours',
            field=models.IntegerField(default=2),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='class_name',
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
        migrations.AddField(
            model_name='subject',
            name='class_name',
            field=models.ManyToManyField(related_name='subjects', to='schedules.class'),
        ),
    ]
