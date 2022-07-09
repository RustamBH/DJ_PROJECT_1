from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(verbose_name='Name', max_length=64)
    price = models.IntegerField(verbose_name='Price')
    image = models.CharField(verbose_name='Image', max_length=128)
    release_date = models.DateField(verbose_name='Release date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(verbose_name='URL', max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
