from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.LogoutPage.as_view(), name="logout"),
    path("", views.HomePage.as_view(), name="index"),
    path("inactive-products", views.ProductInactiveListView.as_view(),
         name="products_inactive"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(),
         name="product_detail"),
    path("product/<int:pk>/edit", views.ProductEditView.as_view(),
         name="product_edit"),
    path("product/new", views.ProductCreateView.as_view(), name='product_create'),
    path("product/<int:pk>/delete",
         views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/<slug:slug>/', views.ProductByCategoryListView.as_view(), name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
