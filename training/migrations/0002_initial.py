# Generated by Django 4.1.7 on 2024-03-14 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationstatus',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='certification',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='certifications', to='users.role'),
        ),
    ]
