from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from longclaw.longclawproducts.models import ProductVariantBase

class ProductVariant(ProductVariantBase):

    _SIZE_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('X-Large', 'X-Large')
    )

    # Enter your custom product variant fields here
    # e.g. colour, size, stock and so on.
    # Remember, ProductVariantBase provides 'price', 'ref', 'slug' fields
    # and the parental key to the Product model.
    description = RichTextField()

    dress_size = models.CharField(max_length=10, choices=_SIZE_CHOICES, default='Medium')