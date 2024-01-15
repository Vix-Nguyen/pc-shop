from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(),
         name="product-detail"),
    path("product/<int:pk>/edit", views.ProductEditView.as_view(),
         name="product-edit"),
    path("product/new", views.ProductCreateView.as_view(), name='create_product'),
    path("product/list", views.ProductListView.as_view(), name='manage_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
