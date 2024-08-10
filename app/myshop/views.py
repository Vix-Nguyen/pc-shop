from typing import Any
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.db.models import Q

from .forms import ImageForm, ProductForm
from .models import Category, Product, ProductImage, Thumbnail


class LoginPage(LoginView):
    template_name = "myshop/login.html"


class LogoutPage(LogoutView):
    next_page = "/login"


class HomePage(ListView):
    model = Category
    template_name = "myshop/index.html"
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["thumnails"] = Thumbnail.objects.all()

        categories = Category.objects.prefetch_related('products').all()
        category_product_dict = {category: category.products.all() for category in categories}
        context['category_product_dict'] = category_product_dict
        return context


class ProductInactiveListView(LoginRequiredMixin, ListView):
    queryset = Product.objects.filter(active=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inactive"] = True
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.get_object()
        context["images"] = ProductImage.objects.filter(product=product_id)
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
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


class ProductEditView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        context["imageform"] = ImageForm()
        context["images"] = ProductImage.objects.filter(product=product)
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        res = super().post(request, *args, **kwargs)
        files = request.FILES.getlist("image")

        if not files:
            return res
        
        product = self.get_object()
        product.images.all().delete()
        for image_file in files:
            ProductImage.objects.create(
                product=product, image=image_file)

        return res


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProductByCategoryListView(ListView):
    model = Product
    template_name = "myshop/product_category.html"

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        slug = self.kwargs['slug']
        context['category'] = get_object_or_404(Category, slug=slug)
        category_product_dict = {context['category']: products}
        context['category_product_dict'] = category_product_dict
        return context

class SearchResultsView(ListView):
    model = Product
    template_name = 'myshop/product_category.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(name__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        categories = Category.objects.prefetch_related('products').all()
        category_product_dict = {category: products.filter(
            category=category) for category in categories if category.products.exists()}
        context['category_product_dict'] = category_product_dict

        query = self.request.GET.get('q')
        context['q'] = query
        return context
