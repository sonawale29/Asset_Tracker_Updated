# Generated by Django 4.2.2 on 2023-06-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_App", "0028_alter_assetmodel_assetcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.UUIDField(
                default="435d0062-971f-460e-872f-0ddbe1786350", editable=False
            ),
        ),
    ]
