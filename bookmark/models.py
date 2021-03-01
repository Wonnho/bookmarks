from django.db import models
from django.urls import reverse
# Create your models here.

class Bookmark(models.Model):
    site_name=models.CharField(max_length=155)
    url=models.URLField('site URL')

    def __str__(self):
        return "name: "+ self.site_name+", address:"+self.url

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])


