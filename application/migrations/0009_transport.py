# Generated by Django 5.0.1 on 2024-05-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_alter_certificates_community_certificate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='transport',
            fields=[
                ('admissionNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Bus_route', models.CharField(blank=True, max_length=100, null=True)),
                ('Bus_stop', models.CharField(blank=True, max_length=100, null=True)),
                ('Bus_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Bus_time', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
