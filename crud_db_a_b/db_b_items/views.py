from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemB

def item_list_b(request):
    items = ItemB.objects.using('db_b').all()
    return render(request, 'db_b_items/item_list.html', {'items': items})

def item_create_b(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        ItemB.objects.using('db_b').create(name=name, description=description)
        return redirect('item_list_b')
    return render(request, 'db_b_items/item_form.html')

def item_edit_b(request, pk):
    item = get_object_or_404(ItemB.objects.using('db_b'), pk=pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save(using='db_b')
        return redirect('item_list_b')
    return render(request, 'db_b_items/item_form.html', {'item': item})

def item_delete_b(request, pk):
    item = get_object_or_404(ItemB.objects.using('db_b'), pk=pk)
    item.delete(using='db_b')
    return redirect('item_list_b')
