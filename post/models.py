from django.db import models

# Create your models here.
class Post(models.Model):
    postTitle = models.TextField(null=True)
    postWriter = models.CharField(null=True, max_length=20)
    postDate = models.CharField(null=True, max_length=200)
    postContent = models.TextField(null=True)
    postUrl = models.TextField(null=True)

    def __str__(self):
        return str(self.postTitle)