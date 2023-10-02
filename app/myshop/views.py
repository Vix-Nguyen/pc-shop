from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .forms import ImageForm, ProductForm
from .models import Product, ProductImage

def index(request):
    product_list = Product.objects.all()
    template = loader.get_template("myshop/index.html")
    context = {
        "product_list": product_list
    }
    return HttpResponse(template.render(context, request))

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.all().filter(product=product_id)
    return render(request, "myshop/product.html", {"product": product, "images": images})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                ProductImage.objects.create(product=f, image=i)
            messages.success(request, "New Product Added")

            return HttpResponseRedirect("/")
        else:
            print(form.errors)
    else:
        form = ProductForm()
        imageform = ImageForm()

    return render(request, "myshop/product_form.html", {"form": form, "imageform": imageform})
