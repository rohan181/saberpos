# Generated by Django 4.0.3 on 2022-08-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_useritem_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useritem',
            name='credit',
            field=models.CharField(choices=[('credit', 'credit'), ('noncredit', 'noncredit')], default='noncredit', max_length=10, null=True),
        ),
    ]