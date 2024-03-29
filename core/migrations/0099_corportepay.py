# Generated by Django 4.0.3 on 2023-04-29 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0098_mrentryrecord_price1'),
    ]

    operations = [
        migrations.CreateModel(
            name='corportepay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.PositiveIntegerField(default=0)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('groupproduct', models.BooleanField(blank=True, null=True)),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
        ),
    ]
