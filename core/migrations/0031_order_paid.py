# Generated by Django 4.0.3 on 2022-07-03 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
