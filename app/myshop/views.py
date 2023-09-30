from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Product

def index(request):
    product_list = Product.objects.all()
    template = loader.get_template("myshop/index.html")
    context = {
        "product_list": product_list
    }
    return HttpResponse(template.render(context, request))

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "myshop/product.html", {"product": product})

def results(request, product_id):
    response = "You're looking at the type of product_id %s."
    return HttpResponse(response % product_id.name)
