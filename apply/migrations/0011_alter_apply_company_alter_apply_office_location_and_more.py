# Generated by Django 5.0.6 on 2024-10-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0010_remove_apply_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='office_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
