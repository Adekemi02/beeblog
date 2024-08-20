from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', 
                                      upload_to='profile',
                                      validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])


    def __str__(self):
        return self.user.username