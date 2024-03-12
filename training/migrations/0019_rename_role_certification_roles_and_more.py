# Generated by Django 4.1.7 on 2024-03-08 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0018_remove_certification_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='role',
            new_name='roles',
        ),
        migrations.AlterField(
            model_name='certificationstatus',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 23, 19, 33, 9, 374629, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='certificationstatus',
            name='scheduled_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 23, 19, 33, 9, 374231, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]