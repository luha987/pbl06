from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemA

def item_list_a(request):
    items = ItemA.objects.using('default').all()
    return render(request, 'items/item_list.html', {'items': items})

def item_create_a(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        ItemA.objects.using('default').create(name=name, description=description)
        return redirect('item_list_a')
    return render(request, 'items/item_form.html')

def item_edit_a(request, pk):
    item = get_object_or_404(ItemA.objects.using('default'), pk=pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save(using='default')
        return redirect('item_list_a')
    return render(request, 'items/item_form.html', {'item': item})

def item_delete_a(request, pk):
    item = get_object_or_404(ItemA.objects.using('default'), pk=pk)
    item.delete(using='default')
    return redirect('item_list_a')
