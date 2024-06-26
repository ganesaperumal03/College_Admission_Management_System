# Generated by Django 5.0.1 on 2024-05-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_alter_personal_details_guardian_father_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_CUT_OFF_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_Chemistry_Mark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_Elective_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_English_Mark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_Language_Mark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_Mathematics_Mark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_PCM_Average',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_Physics_Mark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_aca_Total_Marks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_CUT_OFF_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_English_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Language_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Mathematics_or_Physics_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Mathematics_or_Physics_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_PCM_Average',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Practical_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Total_Marks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Vocational_Theory_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_Vocational_Theory_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hsc_marks',
            name='Twelfth_Std_voc_chemistry_Mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
