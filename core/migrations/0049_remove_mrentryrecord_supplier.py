# Generated by Django 4.0.3 on 2022-08-14 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_remove_mrentryrecord_customer_mrentryrecord_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mrentryrecord',
            name='supplier',
        ),
    ]