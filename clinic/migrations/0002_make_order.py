# Generated by Django 4.2.11 on 2024-04-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Make_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('appointment', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
    ]