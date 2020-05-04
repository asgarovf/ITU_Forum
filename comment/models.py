from homeDir.models import MainPost
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class MainComment(models.Model):
    post = models.ForeignKey(MainPost,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField(verbose_name= ('Yorum'))
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.content
