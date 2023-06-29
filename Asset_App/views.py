import os

from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect
from matplotlib import pyplot as plt
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Asset_App.models import AssetModel, AssetTypeModel
from django.views import View
from django.views.generic.edit import CreateView
from forms import AssetModelRegistration, AssetTpeRegistration
import numpy as np
import csv


# Create your views here.
@login_required(login_url='admin_login')
def AssetEntry(request):
    form_fields = AssetModelRegistration
    context = {"form": form_fields}

    return render(request, "AssetRegistration.html", context)

@login_required(login_url='admin_login')
def Assettypeentry(request):
    form_fields = AssetTpeRegistration
    context = {"form": form_fields}

    return render(request, "Asset_type_registraion.html", context)

@login_required(login_url='admin_login')
def admin_logout(request):
    return redirect("admin_login")


def admin_login(request):
    return render(request, "admin_login2.html")

@login_required(login_url='admin_login')
def assetentry(request, *args, **kwargs):
    form_field = AssetModelRegistration(request.POST)
    if form_field.is_valid():
        try:
            form_field.save()
            return redirect("assetdata")
        except:
            pass
    else:
        form = AssetModelRegistration()
    return render(request, "AssetRegistration.html")

@login_required(login_url='admin_login')
def assettypeentry(request, *args, **kwargs):
    form_field = AssetTpeRegistration(request.POST)
    if form_field.is_valid():
        form_field.save()
        return redirect("assettypedata")


    else:
        return render(request, "Asset_type_registraion.html")



@login_required(login_url='admin_login')
def asset_type_data(request):
    result = AssetTypeModel.objects.all().order_by("-id")

    return render(request, "asset_data_table.html", context={"result": result})

@login_required(login_url='admin_login')
def asset_data(request):
    result = AssetModel.objects.all().order_by("-id")

    return render(request, "Asset_Data_Table.html", context={"result": result})

@login_required(login_url='admin_login')
def admin_panel(request):
    context = {"context": "Hello"}
    uname = request.POST["uname"]
    pass_ = request.POST["pass_"]

    user_authenticate = authenticate(username=uname, password=pass_)
    if user_authenticate is not None:
        return render(request, "simple.html", context)

    return redirect("admin_login")

@login_required(login_url='admin_login')
def delete_asset_type(request):
    result = AssetTypeModel.objects.all()

    return render(request, "delete.html", context={"result": result})

@login_required(login_url='admin_login')
def delete_asset(request):
    result = AssetModel.objects.all()

    return render(request, "Delete_Asset.html", context={"result": result})

@login_required(login_url='admin_login')
def deleteassettype(request, *args, **kwargs):
    find = request._post
    result = AssetTypeModel.objects.filter(id=find.get("assettype"))
    result.delete()
    return redirect("assettypedata")

@login_required(login_url='admin_login')
def deleteasset(request, *args, **kwargs):
    find = request._post
    result = AssetModel.objects.get(pk=find.get("asset"))
    result.delete()
    return redirect("assetdata")

@login_required(login_url='admin_login')
def update(request, *args, **kwargs):
    result = AssetTypeModel.objects.all()
    context = {"result": result}
    return render(request, "update.html", context)

@login_required(login_url='admin_login')
def updaterecord(request):
    data = request._post
    find = data.get("assettype")

    band = AssetTypeModel.objects.get(pk=find)
    form = AssetTpeRegistration(
        instance=band
    )
    return render(request, "Asset_type_update.html", {"form": form, "id": find})

@login_required(login_url='admin_login')
def updatedone(request, id):
    breakpoint()
    result = AssetTypeModel.objects.get(id=id)
    if request.method == "POST":
        form = AssetTpeRegistration(request.POST, instance=result)
    if form.is_valid():
        # update the existing `Band` in the database
        form.save()
        # redirect to the detail page of the `Band` we just updated
        return redirect("assettypedata")

@login_required(login_url='admin_login')
def Assetupdate(request, *args, **kwargs):
    result = AssetModel.objects.all()
    context = {"result": result}
    return render(request, "assetupdate.html", context)

@login_required(login_url='admin_login')
def Assetupdaterecord(request):
    data = request._post
    find = data.get("assettype")
    result = AssetModel.objects.get(pk=find)
    form = AssetModelRegistration(
        instance=result
    )
    return render(request, "asset_update_form.html", {"form": form, "id": find})

@login_required(login_url='admin_login')
def Assetupdatedone(request, id):
    result = AssetModel.objects.get(id=id)
    if request.method == "POST":
        form = AssetModelRegistration(request.POST, instance=result)
    if form.is_valid():
        # update the existing `Band` in the database
        form.save()
        # redirect to the detail page of the `Band` we just updated
        return redirect("assetdata")

@login_required(login_url='admin_login')
def export_to_csv_assetmodel(request):
    data = AssetModel.objects.all()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=AssetDatabase.csv"
    writer = csv.writer(response)
    writer.writerow(
        [
            "AssetName",
            "AssetCode",
            "AssetType",
            "Active_Status",
            "Created_At",
            "Updated_At",
        ]
    )

    for record in data:
        writer.writerow(
            [
                record.AssetName,
                record.AssetCode,
                record.AssetType,
                record.Active_Status,
                record.Created_At,
                record.Updated_At,
            ]
        )
    return response

@login_required(login_url='admin_login')
def export_to_csv_assettypemodel(request):
    data = AssetTypeModel.objects.all()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=AssetTypeRecord.csv"
    writer = csv.writer(response)
    writer.writerow(["Asset_Type", "Asset_Description", "Created_At", "Updated_At"])

    for record in data:
        writer.writerow(
            [
                record.Asset_Type,
                record.Asset_Description,
                record.Created_At,
                record.Updated_At,
            ]
        )
    return response

@login_required(login_url='admin_login')
def piechart(request):
    breakpoint()
    path = '/home/neosoft/PycharmProjects/Asset_Tracker/media/sale_purchase_peichart.png'

    if os.path.isfile(path):
        os.remove(path)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    result1 = AssetTypeModel.objects.all()
    # labels = ['Sale', 'Purchase']
    labels = [x.Asset_Type for x in result1]
    result2 = AssetModel.objects.all()
    sizes = []

    for ele in result1:
        count = AssetModel.objects.all().filter(AssetType=ele.id).count()
        sizes.append(count)
    # sizes = [random.randint(10,30), random.randint(30,50)]
    explode = (0,) * len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90,
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("media/sale_purchase_peichart.png", dpi=100)
    return render(request, "piechart.html")

@login_required(login_url='admin_login')
def barchart(request):
    breakpoint()
    Active = AssetModel.objects.all().filter(Active_Status=True).count()
    Inactive = AssetModel.objects.all().filter(Active_Status=False).count()
    objects = ["Active", "Inactive"]
    y_pos = np.arange(len(objects))
    qty = [Active, Inactive]
    plt.bar(y_pos, qty, align="center", alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Numbers")
    plt.title("Asset Status Report")
    plt.savefig("media/barchart.png")
    return render(request, "barchart.html")

@login_required(login_url='admin_login')
def listing(request):
    contact_list = AssetModel.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})

@login_required(login_url='admin_login')
def band_update(request, id):
    band = AssetTypeModel.objects.get(id=id)
    form = AssetTpeRegistration(
        instance=band
    )
    return render(request, "Asset_type_update.html", {"form": form})
