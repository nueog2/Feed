from django.db import models

# Create your models here.
class FeedComment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(null = True, auto_now_add=True)
    # like = models.TextField(default= '<i class="far fa-heart"></i> ')
    # already_like = models.BooleanField(default=False)
    