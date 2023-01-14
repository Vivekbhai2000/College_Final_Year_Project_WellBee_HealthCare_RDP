# Generated by Django 3.0.4 on 2021-07-12 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0021_orders_ordering_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='ordering_date',
        ),
        migrations.AddField(
            model_name='orders',
            name='orderdate_field',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
