# Generated by Django 4.0.3 on 2024-03-10 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_remove_order_left_remove_product_subpartquantity1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerbalacesheet',
            name='billreceive',
        ),
        migrations.RemoveField(
            model_name='customerbalacesheet',
            name='dueblaceadd',
        ),
        migrations.AddField(
            model_name='customerbalacesheet',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='core.bill'),
        ),
        migrations.AddField(
            model_name='customerbalacesheet',
            name='duebalanceadd',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='customerbalacesheet',
            name='returnn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='returnn', to='core.returnn'),
        ),
    ]
