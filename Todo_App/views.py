from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages


def homepage(request):
    username = request.user
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    items = Item.get_user_items(profile.id)
    
    number = len(items)

    context = {
        'list_items': items,
        'name': 'cherucole',
        'length': number  # if something is referenced above do not put it in quotes because it already has a value so just use name
    }
    return render(request, 'index.html', context)


def item(request, id):
    item = Item.objects.get(id=id)

    context = {
        'list_item': item,
        'name': 'cherucole'
    }
    return render(request, 'details.html', context)

@login_required(login_url='/login/')
def add_item(request):
    current_user = request.user

    if(request.method == 'POST'):
        owner = current_user
        title = request.POST['title']
        body = request.POST['body']

        item = Item(owner=owner, title=title, body=body)
        item.save()

        return redirect('items:homepage')

    else:
        return render(request, 'add.html')

@login_required(login_url='/login/')
def todo_delete(request, id):
    item = get_object_or_404(Item, id=id)  # Get your current item

    if request.method == 'POST':         # If method is POST,

        item.delete()                     # delete the item.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'details.html', {'list_item': item})
    # If method is not POST, render the default template.
