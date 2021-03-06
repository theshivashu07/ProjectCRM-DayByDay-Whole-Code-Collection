# Generated by Django 3.1.7 on 2021-06-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theGuest', '0013_reportstatuses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReportTitle', models.CharField(max_length=30)),
                ('ReportStatus', models.CharField(max_length=15)),
                ('ReportDiscription', models.CharField(max_length=100)),
                ('ReportDate', models.CharField(max_length=10)),
                ('ReportById', models.CharField(max_length=10)),
                ('ReportToId', models.CharField(max_length=10)),
                ('DevsId', models.CharField(max_length=10)),
                ('PMId', models.CharField(max_length=10)),
            ],
        ),
    ]
