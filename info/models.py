from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Info(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_info')
    title = models.TextField(null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title + ' / ' + self.author.username + ' / ' + self.created.strftime('%Y-%m-%d %H:%M:%S')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

