# Generated by Django 3.0.4 on 2020-07-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ai_lab", "0009_auto_20200720_1146"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ailabadoptindexpage",
            options={"verbose_name": "Adopting AI Index Page"},
        ),
        migrations.AlterModelOptions(
            name="ailabdevelopindexpage",
            options={"verbose_name": "Developing AI Index Page"},
        ),
        migrations.AlterModelOptions(
            name="ailabhomepage", options={"verbose_name": "AI Lab Homepage"},
        ),
        migrations.AlterModelOptions(
            name="ailabunderstandindexpage",
            options={"verbose_name": "Understanding AI Index Page"},
        ),
    ]
