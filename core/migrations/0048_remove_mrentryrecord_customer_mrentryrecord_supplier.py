# Generated by Django 4.0.3 on 2022-08-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_mrentryrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mrentryrecord',
            name='customer',
        ),
        migrations.AddField(
            model_name='mrentryrecord',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.supplier'),
        ),
    ]
