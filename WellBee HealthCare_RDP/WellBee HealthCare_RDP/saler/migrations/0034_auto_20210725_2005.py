# Generated by Django 3.0.4 on 2021-07-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0033_doctorregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorregistration',
            name='clinic_Address',
            field=models.TextField(null=True),
        ),
    ]
