"""
URL configuration for Asset_Tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path
from Asset_App import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Asset/',views.AssetEntry,name="AssetEntry"),
    path('assettypeentry/',views.Assettypeentry,name="assettypeentry"),
    path('',views.admin_login,name='admin_login'),
    path('logout',views.admin_login,name='admin_logout'),
    path('adminpanel',views.admin_panel,name='adminpanel'),
    path('assettypedata',views.asset_type_data,name='assettypedata'),
    path('assetdata',views.asset_data,name='assetdata'),
    path('Asset/create',views.assetentry,name='asset'),
    path('assettypeentry/create',views.assettypeentry,name='asset'),
    path('delete/',views.delete_asset_type,name='deleteassettype'),
    path('delete/asset',views.delete_asset,name='deleteasset'),
    path('delete/assettype',views.deleteassettype,name='delete'),
    path('delete/record',views.deleteasset,name='delete'),
    path('update/',views.update,name="updateform"),
    path('update/create',views.updaterecord,name="updaterecord"),
    path('download/AssetModel',views.export_to_csv_assetmodel,name='downloadassetmodel'),
    path('download/AssetType',views.export_to_csv_assettypemodel,name='downloadassettype'),
    path('pie',views.piechart,name='piechart'),
    path('barchart',views.barchart,name="barchart"),
    path('listing',views.listing,name="listing view"),
    path('update/<int:id>',views.updatedone,name="updatepage"),
    path('Assetupdate/',views.Assetupdate,name="assetupdate"),
    path('Assetupdate/create',views.Assetupdaterecord,name="updaterecord"),
    path('Assetupdate/<int:id>',views.Assetupdatedone,name="assetupdatedone"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
