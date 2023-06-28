from django.contrib import admin

# Register your models here.

from Asset_App.models import AssetTypeModel, AssetModel


@admin.register(AssetTypeModel)
class AssetModelType(admin.ModelAdmin):
    list_display = ["id", "Asset_Type", "Asset_Description", "Created_At", "Updated_At"]
    list_filter = ["Asset_Type"]


@admin.register(AssetModel)
class AssetModelType(admin.ModelAdmin):
    list_display = [
        "id",
        "AssetName",
        "AssetCode",
        "AssetType",
        "Active_Status",
        "Created_At",
        "Updated_At",
    ]
