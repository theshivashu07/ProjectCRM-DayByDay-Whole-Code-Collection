# Generated by Django 3.1.7 on 2021-06-24 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theGuest', '0007_auto_20210624_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignProjectToProjectManagerByMyadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProManagerName', models.CharField(max_length=20)),
                ('ProjectName', models.CharField(max_length=30)),
                ('DevsId', models.CharField(max_length=10)),
                ('ProManagerId', models.CharField(max_length=10)),
                ('ProjectId', models.CharField(max_length=10)),
            ],
        ),
    ]
