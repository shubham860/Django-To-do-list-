from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def homepage(request):
    if request.method == "POST":
        form = ListForm(request.POST)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,f"Item has been added to list!")
            return render(request,'todo/home.html',{'all_items':all_items})
    else:
        all_items = List.objects.all()
        return render(request,'todo/home.html',{'all_items':all_items})
