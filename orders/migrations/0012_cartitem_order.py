# Generated by Django 2.0.7 on 2018-08-02 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20180802_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order'),
        ),
    ]
