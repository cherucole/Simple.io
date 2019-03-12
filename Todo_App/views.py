from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def homepage(request):
    items = Item.objects.all()
    number = len(items)
    context = {
        'list_items': items,
        'name': 'cherucole',
        'length': number  # if something is referenced above do not put it in quotes because it already has a value so just use name
    }
    # items = Item.objects.all()
    return render(request, 'index.html', context)


def item(request, id):
    item = Item.objects.get(id=id)
    context = {
        'list_item': item,
        'name': 'cherucole'
    }
    return render(request, 'details.html', context)
