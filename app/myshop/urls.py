from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "myshop"
urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("product/new", views.create_product, name='create_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
