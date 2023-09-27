from django.http import HttpResponse
from django.template import loader

from .models import Product

def index(request):
    product_list = [product for product in Product.objects.order_by("id")]
    template = loader.get_template("myshop/index.html")
    context = {
        "product_list": product_list
    }
    return HttpResponse(template.render(context, request))

def product(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)


def results(request, product_id):
    response = "You're looking at the type of product_id %s."
    return HttpResponse(response % product_id.name)
