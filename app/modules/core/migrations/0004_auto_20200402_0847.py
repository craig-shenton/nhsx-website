# Generated by Django 3.0.4 on 2020-04-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200401_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='headline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='sub_head',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
