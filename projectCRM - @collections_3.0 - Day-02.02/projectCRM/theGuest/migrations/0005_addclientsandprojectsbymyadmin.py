# Generated by Django 3.1.7 on 2021-06-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theGuest', '0004_recruitdeveloperasprojectmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddClientsAndProjectsByMyadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientsFullName', models.CharField(max_length=20)),
                ('ClientsEmailId', models.CharField(max_length=30)),
                ('ClientsMobileNo', models.CharField(max_length=10)),
                ('ProjectName', models.CharField(max_length=30)),
                ('ProjectLanguage', models.CharField(max_length=30)),
                ('ProjectStartDate', models.CharField(max_length=10)),
                ('ProjectLastDate', models.CharField(max_length=10)),
                ('ProjectBudget', models.CharField(max_length=6)),
                ('ClientsUserId', models.CharField(max_length=25)),
                ('ClientsPassword', models.CharField(max_length=25)),
            ],
        ),
    ]
