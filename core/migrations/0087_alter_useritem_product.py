# Generated by Django 4.0.3 on 2023-01-02 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_useritem_groupproduct_alter_useritem_productype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useritem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
