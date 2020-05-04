from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class MainPost(models.Model):
    title = models.CharField(max_length = 50,verbose_name= ('Başlık'))
    content = models.TextField(verbose_name= ('Yazı'))
    date_posted = models.DateTimeField(default=timezone.now)
    url = models.URLField(blank=True,null=True,verbose_name = ('Link (https://...)'))
    tag = models.CharField(max_length=50,verbose_name=('Tag - #'),blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('comment', kwargs={'pk':self.pk})
