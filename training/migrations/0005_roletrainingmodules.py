# Generated by Django 5.0.3 on 2024-04-27 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_profiletrainingevents'),
        ('users', '0012_delete_roletrainingmodules'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleTrainingModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.TextField(blank=True, default='')),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
        ),
    ]
