# Generated by Django 4.1.2 on 2023-12-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="academic_details", name="admission_exit",),
        migrations.AddField(
            model_name="personal_details",
            name="admission_exit",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
