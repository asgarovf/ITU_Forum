from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to = 'profile_pics',verbose_name= ('Resim'))
    bio = models.CharField(max_length=500, blank=True, null=True)
    website_instagram = models.URLField(max_length=100, blank=True, null=True)
    website_facebook = models.URLField(max_length=100, blank=True, null=True)
    website_twitter = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    """
        def save(self,*args, **kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    """
