# Generated by Django 2.1.7 on 2021-03-23 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='assets',
        ),
    ]
