# Generated by Django 3.0.4 on 2021-07-12 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0020_orders_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ordering_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]