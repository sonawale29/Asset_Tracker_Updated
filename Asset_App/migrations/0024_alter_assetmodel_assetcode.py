# Generated by Django 4.2.2 on 2023-06-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0023_auto_20230629_1517"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default="307d3eac-a01c-4dbf-86e9-736ad3c99bec",
                editable=False,
                unique=True,
            ),
        ),
    ]