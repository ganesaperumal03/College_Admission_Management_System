# Generated by Django 5.0.1 on 2024-05-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_rename_twelfth_std_register_no_hsc_marks_twelfth_std_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='hsc_marks',
            name='Twelfth_Std_Register_No',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]