# Generated by Django 4.2.5 on 2024-05-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_hsc_marks_other_eleventh_std_school_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificates',
            fields=[
                ('admissionNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Tenth_mark_sheet', models.CharField(blank=True, max_length=50, null=True)),
                ('eleventh_mark_sheet', models.CharField(blank=True, max_length=50, null=True)),
                ('Twelfth_mark_sheet', models.CharField(blank=True, max_length=50, null=True)),
                ('Transfer_Certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('Community_Certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('First_year_graduate_Certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('Income_Certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('Migration_Certificate', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
