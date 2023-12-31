# Generated by Django 4.2.2 on 2023-06-29 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0005_alter_assetmodel_assetcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.TextField(default="ad0ef38c-27c1-47"),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 35, 31, 564156)
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 35, 31, 564170)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 35, 31, 563595)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 35, 31, 563617)
            ),
        ),
    ]
