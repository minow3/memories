# Generated by Django 3.2.19 on 2023-05-24 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='status',
        ),
    ]
