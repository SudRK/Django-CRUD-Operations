import email
from django.db import models
import uuid

# Create your models here.


class customer(models.Model):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'image/' + filename
    
    name = models.CharField(max_length=72)
    email = models.EmailField(max_length=72)
    password = models.CharField(max_length=72)
    image = models.ImageField(upload_to=get_avatar_path, null=True, blank=True, default="image/default.jpg")