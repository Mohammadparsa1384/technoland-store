# Generated by Django 4.2.5 on 2024-03-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
