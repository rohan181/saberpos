# Generated by Django 4.0.3 on 2022-10-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_remove_customer_bal'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='quantity',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
