# Generated by Django 3.2.16 on 2023-05-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_liked_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
