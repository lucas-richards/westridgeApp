# Generated by Django 4.1.7 on 2024-03-09 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0019_rename_role_certification_roles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificationstatus',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 24, 20, 49, 55, 8343, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='certificationstatus',
            name='scheduled_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 24, 20, 49, 55, 6826, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]