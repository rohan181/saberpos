# Generated by Django 4.0.3 on 2023-02-02 03:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0092_sold_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='paybill',
            name='pettycashbalance',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='paybill',
            name='reloadpetteycash',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
