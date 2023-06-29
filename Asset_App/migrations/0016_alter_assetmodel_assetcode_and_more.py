# Generated by Django 4.2.2 on 2023-06-29 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0015_alter_assetmodel_assetcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default="95cb278e-6538-4269-8bf3-ddfdac0a5eb0", editable=False
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 59, 51, 792404)
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 59, 51, 792418)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 59, 51, 791854)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 59, 51, 791876)
            ),
        ),
    ]
