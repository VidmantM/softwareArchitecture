# Generated by Django 3.2.16 on 2023-04-10 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20230410_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='edited_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
    ]
