from django.db import models

# Create your models here.
class Post(models.Model):
    postTitle = models.TextField(null=True)
    postWriter = models.TextField(null=True)
    postDate = models.TextField(null=True)
    postContent = models.TextField(null=True)
    postUrl = models.TextField(null=True)

    def __str__(self):
        return str(self.postTitle)