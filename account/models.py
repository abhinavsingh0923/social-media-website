from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()

# Create your models here.
class profile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_username=models.IntegerField()
    bio=models.TextField()
    profile_photo=models.ImageField( upload_to='profile_images', default="profile_img.png")
    location=models.CharField( max_length=50, blank=True)


    def __str__(self) -> str:
        return self.user.username 