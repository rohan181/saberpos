# Generated by Django 4.0.3 on 2022-11-22 08:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0080_dailyreport_petteycash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paybill',
            old_name='address',
            new_name='remarks',
        ),
        migrations.CreateModel(
            name='temppaybill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.DecimalField(decimal_places=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('remarks', models.CharField(blank=True, max_length=800, null=True)),
                ('paybillcatogory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.paybillcatogory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
