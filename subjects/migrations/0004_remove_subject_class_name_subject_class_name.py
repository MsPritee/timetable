# Generated by Django 5.1.5 on 2025-02-10 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0009_remove_subject_class_name_subject_class_name'),
        ('subjects', '0003_subject_weekly_hours_remove_subject_class_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='class_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='schedules.class'),
        ),
    ]
