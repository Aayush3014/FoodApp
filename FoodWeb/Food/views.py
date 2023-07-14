from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }

    return render(request,'Food/index.html',context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'Food/detail.html',context)


def item_create(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Food:index')
    
    return render(request, 'Food/item-form.html',{'form':form})


def item_update(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('Food:index')
    return render(request,'Food/item-form.html',{'form':form, 'item':item})


def item_delete(request, id):
    item = Item.objects.get(id=id)

    if request.method =='POST':
        item.delete()
        return redirect('Food:index')
    return render(request, 'Food/item-delete.html', {'item':item})