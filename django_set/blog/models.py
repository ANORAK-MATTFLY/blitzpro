from froala_editor.fields import FroalaField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='porfile_pics')

    def __str__(self):
        return f'{self.user.username} profile'



class Post(models.Model):
    title = models.CharField(max_length=70)
    tag = models.CharField(max_length=30, default='Programming')
    content_overview = models.CharField(max_length=200)
    content = FroalaField(theme='dark')
    date_post = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    email = models.EmailField()
    singnup_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

