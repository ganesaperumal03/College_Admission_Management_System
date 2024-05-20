# Generated by Django 5.0.1 on 2024-05-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_personalform_alter_preform_profile_image_and_more'),
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
        migrations.CreateModel(
            name='GQ_Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=50)),
                ('Tuition_Fees', models.CharField(max_length=50)),
                ('CoExtra_Curricularfees', models.CharField(max_length=50)),
                ('Development_fees', models.CharField(max_length=50)),
                ('Learning_Materials_Platform_UniformFees', models.CharField(max_length=50)),
                ('Caution_Deposit', models.CharField(max_length=50)),
                ('Hostel', models.CharField(blank=True, max_length=50, null=True)),
                ('Dayscholar', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MQ_Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=50)),
                ('Tuition_Fees', models.CharField(max_length=50)),
                ('CoExtra_Curricularfees', models.CharField(max_length=50)),
                ('Development_fees', models.CharField(max_length=50)),
                ('Learning_Materials_Platform_UniformFees', models.CharField(max_length=50)),
                ('Caution_Deposit', models.CharField(max_length=50)),
                ('Hostel', models.CharField(blank=True, max_length=50, null=True)),
                ('Dayscholar', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='personalform',
            old_name='Residental_Address_Line_1',
            new_name='place',
        ),
        migrations.RemoveField(
            model_name='personalform',
            name='Date_of_Birth',
        ),
        migrations.RemoveField(
            model_name='personalform',
            name='Father_Mobile_Number',
        ),
        migrations.RemoveField(
            model_name='personalform',
            name='Hostel_Required',
        ),
        migrations.RemoveField(
            model_name='personalform',
            name='Self_Email_ID',
        ),
        migrations.RemoveField(
            model_name='personalform',
            name='Self_Mobile_Number',
        ),
        migrations.RemoveField(
            model_name='personalform',
            name='whatsapp_number',
        ),
        migrations.AddField(
            model_name='academic_details',
            name='academic_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hsc_marks',
            name='other_Eleventh_Std_School_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hsc_marks',
            name='other_Twelfth_Std_School_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='academic_Category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='other_Tenth_Std_School_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personalform',
            name='Mobile_Number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='personalform',
            name='year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
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
        migrations.AlterField(
            model_name='personal_details',
            name='Guardian_Father_Mobile_No',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='personalform',
            name='Father_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalform',
            name='gm_conform',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
