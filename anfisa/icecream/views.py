from django.shortcuts import render
from .models import icecream_db


def icecream_details(request, pk):
    name = icecream_db[pk]['name']
    description = icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream_detail.html', context)
