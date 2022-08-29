# Generated by Django 3.0.14 on 2022-08-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220827_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
