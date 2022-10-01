from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)