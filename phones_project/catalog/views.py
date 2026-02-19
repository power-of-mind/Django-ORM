from django.shortcuts import render, get_object_or_404
from .models import Phone

def catalog_view(request):
    sort = request.GET.get('sort')

    phones = Phone.objects.all()

    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')

    return render(request, 'catalog/catalog.html', {
        'phones': phones
    })

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    return render(request, 'catalog/product.html', {
        'phone': phone
    })