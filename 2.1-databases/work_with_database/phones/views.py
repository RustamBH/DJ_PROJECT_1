from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_type = request.GET.get("sort")
    template = 'catalog.html'

    if sort_type == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort_type == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort_type == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    else:
        phone_objects = Phone.objects.all()

    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
