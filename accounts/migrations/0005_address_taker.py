# Generated by Django 4.2.5 on 2024-02-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_address_province_alter_address_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='taker',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
