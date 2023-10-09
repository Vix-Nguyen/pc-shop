from django import forms

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    thumbnail = forms.ImageField(label="Thumbnail")

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "thumbnail",
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = ProductImage
        fields = ("image",)
