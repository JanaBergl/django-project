# Generated by Django 4.2 on 2025-03-10 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plant_care', '0007_alter_plant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantcarehistory',
            name='task_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
