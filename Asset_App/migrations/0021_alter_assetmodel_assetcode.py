# Generated by Django 4.2.2 on 2023-06-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0020_alter_assetmodel_assetcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default="29fcd0b6-2c9a-4e8c-bc8c-dfd60ae81b15", editable=False
            ),
        ),
    ]
