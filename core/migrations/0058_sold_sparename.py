# Generated by Django 4.0.3 on 2022-09-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_useritem_sparename'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold',
            name='sparename',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
