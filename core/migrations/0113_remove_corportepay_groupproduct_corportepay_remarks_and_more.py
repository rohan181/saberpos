# Generated by Django 4.0.3 on 2024-02-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0112_corpocatagory_remove_corportepay_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corportepay',
            name='groupproduct',
        ),
        migrations.AddField(
            model_name='corportepay',
            name='remarks',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='remarks',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]