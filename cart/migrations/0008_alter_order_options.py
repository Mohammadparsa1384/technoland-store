# Generated by Django 5.0.1 on 2024-03-24 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_rename_order_order_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارش ها'},
        ),
    ]
