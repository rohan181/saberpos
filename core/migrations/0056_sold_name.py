# Generated by Django 4.0.3 on 2022-08-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_alter_customer_options_sold_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
