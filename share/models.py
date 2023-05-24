from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
import uuid

user = get_user_model()


class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        user, related_name="uploads", on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='liked_images', blank=True)

    class Meta:
        ordering = ['-created']
