from email import message
from multiprocessing import context
import os
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import CustomerRegisteration
from .models import customer
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# This funtion will add data to the database.
def add_show(request, id="None"):
    if request.method == "POST":
        fm = CustomerRegisteration(request.POST, request.FILES)
        if fm.is_valid():
            # nm = fm.cleaned_data["name"]
            # em = fm.cleaned_data["email"]
            # pwd = fm.cleaned_data["password"]
            # img = fm.cleaned_data["image"]
            # reg = customer(name=nm, email=em, password=pwd, image=img)
            # reg.set_password(pwd)
            # using this method we can save individual data of each fields.
            # reg.save()
            fm.save()
            fm = (
                CustomerRegisteration()
            )  # this saves data directly inserted into fields
    else:
        fm = CustomerRegisteration()
    cust = customer.objects.all()
    return render(request, "enroll/addnshow.html", {"form": fm, "cus": cust})


# This function will update data from database


def update(request, id):
    pid = customer.objects.get(pk=id)
    fm = CustomerRegisteration(request.POST, request.FILES)
    if request.method == "POST":
        if fm.is_valid():
            if request.FILES:
                pid.image = request.FILES['image']
            fm = CustomerRegisteration(request.POST, instance=pid)
            fm.save()
            fm = CustomerRegisteration()
            return HttpResponseRedirect(reverse("addnshow"))
    pid = customer.objects.get(pk=id)
    fm = CustomerRegisteration(instance=pid)
    cust = customer.objects.all()
    return render(request, "enroll/addnshow.html", {"form": fm, "cus": cust})
    

# This function will delete data from database


def delt(request, id):
    if request.method == "POST":
        pid = customer.objects.get(pk=id)
        pid.delete()
        return HttpResponseRedirect("/")


def filter(request):
    if request.method == "POST":
        name = request.POST.get("search")
        fil = customer.objects.filter(name__contains=name).all()
        fm = CustomerRegisteration()
        return render(
            request, "enroll/addnshow.html", {"form": fm, "cus": fil, "name": name}
        )
