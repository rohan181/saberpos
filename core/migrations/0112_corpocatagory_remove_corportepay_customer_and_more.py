# Generated by Django 4.0.3 on 2024-02-08 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0111_dailyreport_returncostprice_alter_returnn_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='corpocatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='corportepay',
            name='Customer',
        ),
        migrations.AddField(
            model_name='corportepay',
            name='suppiler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.supplier'),
        ),
        migrations.AddField(
            model_name='corportepay',
            name='corpocatagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.corpocatagory'),
        ),
    ]
