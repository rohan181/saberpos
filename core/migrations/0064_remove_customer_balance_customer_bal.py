# Generated by Django 4.0.3 on 2022-10-22 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_customer_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='balance',
        ),
        migrations.AddField(
            model_name='customer',
            name='bal',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
