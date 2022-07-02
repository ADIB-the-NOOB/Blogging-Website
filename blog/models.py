from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.utils.text import slugify
# Create your models here.


class PostCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    category = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='blogimg')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height >= 2160 or img.width >= 3840:
            output_size = (1920, 1080)
            img.thumbnail(output_size)
            img.save(self.image.path)
        


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.EmailField()
    comment = models.TextField()
    dateadded = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-dateadded']

    def __str__(self):
        return self.comment[0:10]
