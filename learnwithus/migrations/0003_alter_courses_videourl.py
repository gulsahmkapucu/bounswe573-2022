# Generated by Django 3.2.13 on 2022-05-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnwithus', '0002_courses_videourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='videourl',
            field=models.FileField(upload_to='video/%y'),
        ),
    ]
