from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Feed_Post(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(null = True, auto_now_add=True)
    like = models.BooleanField(default=False)
    #already_like = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    

class Comment(models.Model):
    content = models.TextField(default="빈 댓글입니다.")
    post = models.ForeignKey(Feed_Post,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(null = True, auto_now_add=True)
    
    class Meta:
        db_table = 'comments'

    

# class User(models.Model):
#     username = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'users'
