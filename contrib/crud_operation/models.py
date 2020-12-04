from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('news:news_view', kwargs={'id': self.id})