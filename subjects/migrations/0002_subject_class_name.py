# Generated by Django 5.1.5 on 2025-02-10 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='class_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
