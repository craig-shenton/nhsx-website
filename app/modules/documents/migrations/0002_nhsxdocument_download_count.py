# Generated by Django 3.0.7 on 2020-10-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nhsxdocument",
            name="download_count",
            field=models.IntegerField(default=0),
        ),
    ]
