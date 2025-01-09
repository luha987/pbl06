from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemA

def item_list(request):
    items = ItemA.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def item_create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        ItemA.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'items/item_form.html')

def item_edit(request, pk):
    item = get_object_or_404(ItemA, pk=pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request, 'items/item_form.html', {'item': item})

def item_delete(request, pk):
    item = get_object_or_404(ItemA, pk=pk)
    item.delete()
    return redirect('item_list')
