from typing import Any
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)

from .forms import ImageForm, ProductForm
from .models import Product, ProductImage


class HomePage(ListView):
    model = Product
    template_name = "myshop/index.html"


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.get_object()
        context["images"] = ProductImage.objects.filter(product=product_id)
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imageform"] = ImageForm()
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = ProductForm(request.POST, request.FILES)
        files = request.FILES.getlist("image")

        if form.is_valid():
            product_instance = form.save(commit=False)
            product_instance.user = request.user
            product_instance.save()

            for image_file in files:
                ProductImage.objects.create(
                    product=product_instance, image=image_file)

            messages.success(request, 'New Product Added')

            return redirect(
                reverse(
                    'product_detail',
                    kwargs={'pk': product_instance.pk}
                ))
        else:
            return HttpResponse(form.errors)


class ProductEditView(UpdateView):
    model = Product
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imageform"] = ImageForm()
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
