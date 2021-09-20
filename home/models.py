from django.db import models
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('H', 'Helmets'),
    ('B', 'Boots'),
    ('O', 'Outwear'),
    ('A', 'Accessories')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Carousel(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=100, blank=True)
    link_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=140)
    friendly_title = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.title

    def get_friendly_title(self):
        return self.friendly_title


class Item(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    category2 = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    sku = models.CharField(max_length=140, blank=True)
    title = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.FileField(
        upload_to='product_image', blank=True
    )
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })
