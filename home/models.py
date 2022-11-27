from django.db import models
import uuid

# Create your models here.

class post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    user =models.CharField( max_length=100)
    image=models.ImageField( upload_to='post_images')
    caption=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user
    

class likepost(models.Model):
    post_id=models.CharField( max_length=500)
    username=models.CharField( max_length=500)

    def __str__(self):
        return self.username
    
class followercount(models.Model):
    follower = models.CharField( max_length=500)
    user =models.CharField( max_length=500)

    def __str__(self):
        return self.user
    