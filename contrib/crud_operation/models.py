from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('news:news_view', kwargs={'id': self.id})