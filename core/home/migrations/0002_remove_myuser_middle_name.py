# Generated by Django 4.2 on 2024-09-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='middle_name',
        ),
    ]
