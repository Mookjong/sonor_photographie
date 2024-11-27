from django.db import models

# Create your models here.


class Tag(models.Model):
    class Meta:
        verbose_name = "Catégorie"

    name = models.CharField(
        verbose_name="nom", unique=True, null=False, blank=False, max_length=100
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(
        verbose_name="nom", unique=True, null=False, blank=False, max_length=100
    )

    description = models.TextField(null=True, blank=True, max_length=300)

    image = models.ImageField(
        # images will be uploaded to /media/uploads/products
        upload_to="uploads/images/"
    )

    tags = models.ManyToManyField(
        to=Tag,
    )

    def __str__(self):
        return self.name
