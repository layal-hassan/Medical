# Generated by Django 4.1.7 on 2024-04-29 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_make_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make_order',
            name='appointment',
        ),
    ]
