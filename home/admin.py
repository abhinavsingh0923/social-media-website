from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(post)
admin.site.register(likepost)
admin.site.register(followercount)