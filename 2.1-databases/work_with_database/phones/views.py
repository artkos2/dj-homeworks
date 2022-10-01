from .models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    template = 'catalog.html'
    context = {}
    if sort == 'max_price':
        phones_objects = Phone.objects.all().order_by('-price')
    elif sort == 'min_price':
        phones_objects = Phone.objects.all().order_by('price')
    else:
        phones_objects = Phone.objects.all().order_by('name')
    context = {'phones': phones_objects}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phones_objects = Phone.objects.all().filter(slug=slug)
    context = {'phones': phones_objects}
    return render(request, template, context)
