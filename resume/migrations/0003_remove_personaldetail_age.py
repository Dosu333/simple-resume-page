# Generated by Django 3.1.13 on 2021-08-18 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20210818_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='age',
        ),
    ]
