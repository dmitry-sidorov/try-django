from django.shortcuts import render
from .models import Product
from .forms import ProductFrom


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductFrom(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductFrom()

    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)
