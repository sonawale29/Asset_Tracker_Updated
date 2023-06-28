from django.db import models
from utility import generate_asset_code
from datetime import datetime
import uuid
import time

# Create your models here.


class AssetTypeModel(models.Model):
    Asset_Type = models.TextField(unique=True)
    Asset_Description = models.TextField(max_length=500)
    Created_At = models.DateTimeField(default=datetime.now())
    Updated_At = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Asset_Type


class AssetModel(models.Model):
    AssetName = models.TextField()
    AssetCode = models.TextField(
        unique=True, default=time.time()
    )
    AssetType = models.ForeignKey(
        AssetTypeModel, on_delete=models.CASCADE
    )  # Relationship establish between the Asset
    # type and Asset i.e one-many relation using ORM.
    Active_Status = models.BooleanField(default=True)
    Created_At = models.DateTimeField(default=datetime.now())
    Updated_At = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.AssetCode
