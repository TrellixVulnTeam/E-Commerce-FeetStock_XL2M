# Generated by Django 3.0.14 on 2022-08-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220826_2024'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='order',
            constraint=models.UniqueConstraint(condition=models.Q(complete=False), fields=('customer',), name='incomplete_order_per_customer'),
        ),
    ]
