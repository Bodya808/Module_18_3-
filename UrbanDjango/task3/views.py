from django.shortcuts import render

def home_view(request):
    return render(request, 'third_task/home.html')

def store_view(request):
    items = {
        'item1': {'name': 'WuKong', 'price': '$10'},
        'item2': {'name': 'RDR2', 'price': '$20'},
        'item3': {'name': 'Cyber Punk', 'price': '$30'}
    }
    context = {'items': items}
    return render(request, 'third_task/store.html', context)

def cart_view(request):
    return render(request, 'third_task/cart.html')