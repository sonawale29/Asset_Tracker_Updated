# Generated by Django 4.2.2 on 2023-06-29 09:28

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0013_alter_assetmodel_assetcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default=uuid.UUID("a9c6a8ec-afa0-4518-a0b2-1d807d14cfa4"),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 58, 22, 914180)
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 58, 22, 914195)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 58, 22, 913625)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 29, 14, 58, 22, 913647)
            ),
        ),
    ]
