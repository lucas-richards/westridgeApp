# Generated by Django 4.1.7 on 2024-03-08 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0012_alter_certificationstatus_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificationstatus',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 23, 18, 41, 35, 423663, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='certificationstatus',
            name='scheduled_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 23, 18, 41, 35, 423230, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]