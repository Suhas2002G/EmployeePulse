# Generated by Django 5.1.6 on 2025-03-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='dept_name',
            field=models.CharField(max_length=100),
        ),
    ]
