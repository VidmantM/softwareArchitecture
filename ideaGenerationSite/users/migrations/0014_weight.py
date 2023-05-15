# Generated by Django 3.2.16 on 2023-05-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20230417_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(default='name', max_length=30, verbose_name='Name of the formula')),
                ('formula', models.CharField(default='0', max_length=30, verbose_name='Mathematical weight formula')),
            ],
        ),
    ]
