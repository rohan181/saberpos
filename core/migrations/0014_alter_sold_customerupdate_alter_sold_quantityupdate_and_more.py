# Generated by Django 4.0.3 on 2022-06-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='customerupdate',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sold',
            name='quantityupdate',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='useritem',
            name='customerupdate',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='useritem',
            name='quantityupdate',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
