from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from PIL import image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='porfile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    # def save(self):
    #     super().save()
    #     img = image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)



class Post(models.Model):
    title = models.CharField(max_length=70)
    content_overview = models.CharField(max_length=50)
    content = models.TextField()
    date_post = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()

    def __str__(self):
        return self.title
