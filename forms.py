from django.forms import ModelForm
from Asset_App.models import AssetModel,AssetTypeModel


class AssetModelRegistration(ModelForm):
    """ Created form field using the ModelForm for the front-end """
    class Meta:
        model = AssetModel
        fields = ['AssetName','AssetType','Active_Status']

class AssetTpeRegistration(ModelForm):
    """ Created form field using the ModelForm for the front-end """
    class Meta:
        model = AssetTypeModel
        fields = ['id','Asset_Type','Asset_Description']