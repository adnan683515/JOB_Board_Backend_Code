# Generated by Django 5.0.6 on 2024-09-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_alter_job_employment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='office_picture',
            field=models.ImageField(blank=True, null=True, upload_to='officePhoto'),
        ),
    ]
