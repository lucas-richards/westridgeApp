# Generated by Django 4.1.7 on 2024-02-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_birthdate'),
        ('training', '0003_rename_completion_status_certificationstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='department',
            field=models.ManyToManyField(to='users.department'),
        ),
    ]
