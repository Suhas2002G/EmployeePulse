# Generated by Django 5.1.6 on 2025-02-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='dept_name',
            field=models.CharField(choices=[('IT', 'IT'), ('Support', 'Support'), ('Sales', 'Sales')], max_length=100),
        ),
    ]
