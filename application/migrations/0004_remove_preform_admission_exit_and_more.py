# Generated by Django 5.0.1 on 2024-01-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_preform_alter_diplomo_year_of_passing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preform',
            name='admission_exit',
        ),
        migrations.AddField(
            model_name='preform_other_info',
            name='Department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='preform_other_info',
            name='admission_exit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
