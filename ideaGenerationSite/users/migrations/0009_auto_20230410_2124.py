# Generated by Django 3.2.16 on 2023-04-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, to='users.Interest'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(blank=True, to='users.Project'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='users.Skill'),
        ),
    ]
