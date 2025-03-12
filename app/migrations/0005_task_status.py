# Generated by Django 5.1.6 on 2025-03-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In-Progress', 'In-Progress'), ('Completed', 'Completed')], default='Pending', max_length=15),
        ),
    ]
