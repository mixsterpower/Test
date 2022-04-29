from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='image_blog', default='')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(auto_now=True, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, blank=False)
    slug = models.SlugField(max_length=255, null=True, unique=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail',args=[self.slug])