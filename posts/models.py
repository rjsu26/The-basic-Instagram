from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title=models.TextField()
    cover=models.ImageField(upload_to='images/')
    date= models.DateTimeField(default=timezone.now())
    # class Meta:
    #     ordering=['date']

    def __str__(self):
        return self.title
