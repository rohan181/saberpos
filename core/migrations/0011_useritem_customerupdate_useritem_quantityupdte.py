# Generated by Django 4.0.3 on 2022-06-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_order_useritem_order_useritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritem',
            name='customerupdate',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='useritem',
            name='quantityupdte',
            field=models.PositiveIntegerField(default=0),
        ),
    ]