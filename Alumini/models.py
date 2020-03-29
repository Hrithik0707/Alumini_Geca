from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class events(models.Model):
    eve = models.TextField()
    img = models.ImageField(upload_to = 'mydocs',default = None)

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title