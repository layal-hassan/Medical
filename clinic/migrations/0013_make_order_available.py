# Generated by Django 4.2.11 on 2024-05-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_remove_make_order_avilable'),
    ]

    operations = [
        migrations.AddField(
            model_name='make_order',
            name='available',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
