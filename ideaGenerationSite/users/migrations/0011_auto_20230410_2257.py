# Generated by Django 3.2.16 on 2023-04-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20230410_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggedwhatever',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='taggedwhatever',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='tags',
        ),
        migrations.AddField(
            model_name='interest',
            name='expertise',
            field=models.CharField(default='Intermediate', max_length=30, verbose_name='Skill level'),
        ),
        migrations.AddField(
            model_name='interest',
            name='name',
            field=models.CharField(default='name', max_length=30, verbose_name='Name of subject'),
        ),
        migrations.AddField(
            model_name='skill',
            name='expertise',
            field=models.CharField(default='Intermediate', max_length=30, verbose_name='Skill level'),
        ),
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(default='name', max_length=30, verbose_name='Name of subject'),
        ),
        migrations.DeleteModel(
            name='MyCustomTag',
        ),
        migrations.DeleteModel(
            name='TaggedWhatever',
        ),
    ]