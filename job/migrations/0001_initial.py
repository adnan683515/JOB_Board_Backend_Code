# Generated by Django 5.0.6 on 2024-09-07 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('age_limit', models.CharField(max_length=40)),
                ('work_station', models.CharField(max_length=100)),
                ('employment_status', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=100)),
                ('application_date', models.DateField()),
                ('experience', models.TextField()),
                ('education', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('company_information', models.TextField()),
                ('other_benefits', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=30)),
                ('Browse_cetagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.browse_cetagory')),
                ('organizationtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.organizationtype')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.place')),
            ],
        ),
    ]
