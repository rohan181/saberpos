# Generated by Django 4.0.3 on 2022-12-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_paybill_added_paybill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useritem',
            name='exchange_engine',
        ),
        migrations.RemoveField(
            model_name='useritem',
            name='groupproduct',
        ),
        migrations.AlterField(
            model_name='useritem',
            name='productype',
            field=models.CharField(choices=[('LocalContainer', ' LocalContainer'), ('publicContainer', 'publicContainer')], default='Local', max_length=100, null=True),
        ),
    ]
