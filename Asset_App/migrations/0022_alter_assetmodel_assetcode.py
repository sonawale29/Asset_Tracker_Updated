# Generated by Django 4.2.2 on 2023-06-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0021_alter_assetmodel_assetcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default="10c49727-6a6d-4286-a42a-f1b34effa97d", editable=False
            ),
        ),
    ]
