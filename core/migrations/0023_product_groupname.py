# Generated by Django 4.0.3 on 2022-06-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_product_sellprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='groupname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
