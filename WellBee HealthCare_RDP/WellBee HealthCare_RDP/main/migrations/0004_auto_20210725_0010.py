# Generated by Django 3.0.4 on 2021-07-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210624_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='slotdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='slottime',
            field=models.CharField(choices=[('5:00AM-6:00AM', '5:00AM-6:00AM'), ('6:00AM-7:00AM', '6:00AM-7:00AM'), ('7:00AM-8:00AM', '7:00AM-8:00AM'), ('8:00AM-9:00AM', '8:00AM-9:00AM'), ('9:00AM-10:00AM', '9:00AM-10:00AM'), ('10:00AM-11:00AM', '10:00AM-11:00AM'), ('11:00AM-12:00PM', '11:00AM-12:00PM')], max_length=30, null=True),
        ),
    ]
