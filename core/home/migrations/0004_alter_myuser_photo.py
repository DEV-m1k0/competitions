# Generated by Django 4.2.16 on 2024-09-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_myuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='photo',
            field=models.ImageField(upload_to='data/'),
        ),
    ]
