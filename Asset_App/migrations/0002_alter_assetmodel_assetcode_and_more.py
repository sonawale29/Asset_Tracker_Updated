# Generated by Django 4.2.2 on 2023-06-26 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.TextField(default="fbad43e9-daa9-4aa9"),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 26, 5, 10, 15, 223816)
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 26, 5, 10, 15, 223849)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 26, 5, 10, 15, 223351)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 26, 5, 10, 15, 223366)
            ),
        ),
    ]