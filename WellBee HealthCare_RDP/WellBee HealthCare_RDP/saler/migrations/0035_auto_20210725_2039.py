# Generated by Django 3.0.4 on 2021-07-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0034_auto_20210725_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorregistration',
            name='letterhead',
        ),
        migrations.AddField(
            model_name='doctorregistration',
            name='letter_head',
            field=models.FileField(default='default.png', upload_to='doctor_letterhead'),
        ),
    ]
