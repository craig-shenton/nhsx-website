# Generated by Django 3.0.4 on 2020-04-09 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200409_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionpage',
            name='headline',
        ),
    ]
