from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('Food/index.html')
    context = {}

    return HttpResponse(template.render(context,request))