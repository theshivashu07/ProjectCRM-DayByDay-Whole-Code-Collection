# Generated by Django 3.1.7 on 2021-06-24 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theGuest', '0006_auto_20210624_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitdeveloperasprojectmanager',
            name='DevsId',
            field=models.CharField(max_length=10),
        ),
    ]
