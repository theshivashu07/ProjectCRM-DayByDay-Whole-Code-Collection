# Generated by Django 3.1.7 on 2021-06-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theGuest', '0011_assignprojecttodeveloperbyprojectmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProManagerId', models.CharField(max_length=10)),
                ('ProManagerName', models.CharField(max_length=20)),
                ('Status', models.CharField(max_length=10)),
            ],
        ),
    ]
