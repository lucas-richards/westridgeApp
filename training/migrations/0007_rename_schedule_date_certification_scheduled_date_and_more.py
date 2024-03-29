# Generated by Django 4.1.7 on 2024-03-21 01:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_certification_exp_months_certification_schedule_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='schedule_date',
            new_name='scheduled_date',
        ),
        migrations.AlterField(
            model_name='certificationstatus',
            name='completed_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 4, 5, 1, 37, 35, 836021, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
