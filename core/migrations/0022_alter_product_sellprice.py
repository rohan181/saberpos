# Generated by Django 4.0.3 on 2022-06-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_product_sellprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sellprice',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
