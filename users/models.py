from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=255, null=True)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.user.username
    

    def save(self,  *args, **kwargs):
        super().save()
        if self.img:

            img = Image.open(self.img.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.img.path)