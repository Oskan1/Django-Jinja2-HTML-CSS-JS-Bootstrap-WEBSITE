from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # 1-n Relation
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # we want to pass the value, not execute -> now()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # we delete all posts, if user deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

