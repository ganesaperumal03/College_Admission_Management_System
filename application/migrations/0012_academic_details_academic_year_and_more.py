# Generated by Django 5.0.1 on 2024-05-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_alter_hsc_marks_twelfth_std_aca_cut_off_mark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_details',
            name='academic_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='academic_Category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]