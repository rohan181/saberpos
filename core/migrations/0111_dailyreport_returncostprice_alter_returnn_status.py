# Generated by Django 4.0.3 on 2023-09-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0110_returnn_cashreturnprice_returnn_duereturnprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='returncostprice',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='returnn',
            name='status',
            field=models.CharField(choices=[('CASH RETUEN', 'CASH RETUEN'), (' WITH OUT CASH RETUEN', 'WITH OUT CASH RETUEN'), (' BOTH', 'BOTH')], default='CASH RETUEN', max_length=50, null=True),
        ),
    ]