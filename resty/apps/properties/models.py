import os
import uuid
from django.utils import timezone
from django.db import models


def image_path_post(self, filename):
    today = timezone.now()
    path = "{0}/{1}/{2}/".format(today.year, today.month, today.day)
    ext = filename.split('.')[-1]
    my_filename = "{0}.{1}".format(str(uuid.uuid1()).replace('-', ''), ext)
    url = os.path.join(path, my_filename)
    return url


class House(models.Model):
    code = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=image_path_post, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "properties"
        verbose_name = "Casa"
        verbose_name_plural = "Casas"
