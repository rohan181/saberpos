# Generated by Django 4.0.3 on 2022-06-07 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_useritem_customerupdate_useritem_quantityupdte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useritem',
            old_name='quantityupdte',
            new_name='quantityupdate',
        ),
    ]