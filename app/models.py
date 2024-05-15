from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    slug = models.SlugField(max_length=200)
