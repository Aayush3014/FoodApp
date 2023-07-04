from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }

    return render(request,'Food/index.html',context)
