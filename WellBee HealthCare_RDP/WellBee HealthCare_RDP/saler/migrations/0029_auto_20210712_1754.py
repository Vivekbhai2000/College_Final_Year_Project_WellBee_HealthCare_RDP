# Generated by Django 3.0.4 on 2021-07-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0028_auto_20210712_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='orders',
            name='deliverycharge',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='orders',
            name='gstprice',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='orders',
            name='itemprice',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_type',
            field=models.CharField(choices=[('COD', 'COD'), ('Online Payment', 'Online Payment')], default='COD', max_length=15),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_failreason',
            field=models.TextField(default='No Reason'),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(choices=[('Success', 'Success'), ('Failure', 'Failure')], default='Failure', max_length=15),
        ),
        migrations.AddField(
            model_name='orders',
            name='totalprice',
            field=models.CharField(default='0', max_length=10),
        ),
    ]