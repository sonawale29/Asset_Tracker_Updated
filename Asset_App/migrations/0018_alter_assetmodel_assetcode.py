# Generated by Django 4.2.2 on 2023-06-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0017_alter_assetmodel_assetcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default="29de03c3-88b1-4d78-8abc-3b1d6a6c7a2f", editable=False
            ),
        ),
    ]