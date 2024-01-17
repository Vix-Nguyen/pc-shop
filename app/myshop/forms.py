from django import forms

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    thumbnail = forms.ImageField(label="Thumbnail")

    class Meta:
        model = Product
        fields = "__all__"


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        required=False,
    )

    class Meta:
        model = ProductImage
        fields = ("image",)
