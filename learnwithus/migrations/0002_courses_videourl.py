# Generated by Django 3.2.13 on 2022-05-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnwithus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='videourl',
            field=models.TextField(default='https://www.youtube.com/watch?v=UojXOLmzmz0'),
            preserve_default=False,
        ),
    ]
