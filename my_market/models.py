from django.db import models
from django.utils.text import slugify
from account.models import Profile


class Store(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    slug = models.SlugField(null=False, blank=True, db_index=True)
    profiles = models.ManyToManyField(Profile)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, db_index=True)
    stores = models.ForeignKey(Store, on_delete=models.CASCADE)
    profiles = models.ManyToManyField(Profile)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
