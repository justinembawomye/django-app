from django.db import models
from django.contrib.auth.models import User
from PIL import  Image

# Public User models.

class Profile(models.Model):

    """User profile class"""

    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')

    def __str__(self):
        return f"{self.user.username} Profile"


    def save(self):
        """Function to help us resize the image"""
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



