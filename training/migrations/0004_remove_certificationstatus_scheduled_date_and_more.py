# Generated by Django 4.1.7 on 2024-03-21 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_alter_certificationstatus_due_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificationstatus',
            name='scheduled_date',
        ),
        migrations.AddField(
            model_name='certificationstatus',
            name='completed_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 4, 5, 1, 21, 17, 325572, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='certificationstatus',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 4, 5, 1, 21, 17, 327658, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
