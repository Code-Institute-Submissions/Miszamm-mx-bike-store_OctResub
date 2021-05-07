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
    description = models.TextField(null=True)
    link = models.CharField(max_length=100, null=True)
    link_text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField(2)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.FileField(
        upload_to='product_image', null=True
    )
    additional_information = models.TextField(null=True)

    def __str__(self):
        return self.title

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })
