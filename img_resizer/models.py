from django.core.exceptions import FieldError
from django.db import models
import requests
import shutil
from django.conf import settings
from requests.models import parse_header_links
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    picture = models.ImageField(blank=True, null = True, width_field="width", height_field="height")
    width = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    parent_picture = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if (self.url and self.picture) or (not self.url and not self.picture):
            raise FieldError("Error in url or/and picture field")
        else:
            if self.url:
                self.get_image_from_url(self.url)
            self.name = self.picture.name 
            super().save(*args, **kwargs)


    def get_image_from_url(self, url):
        """Get image from url and save it in MEDIA_ROOT folder"""

        response = requests.get(url, stream=True)
        if response.status_code == 200 and "image" in str(response.headers):
            filename = self.parse_image_filename_from_url(self.url)
            with open(settings.MEDIA_ROOT + "/" + filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
                self.picture = filename
            
    def parse_image_filename_from_url(self, url):
        """Parse image name and ext from URL"""
        
        image_name = url.split("/")[-1]
        return image_name

