from django.contrib import admin
from .models import Feed_Post, Comment #,Comment_User

# Register your models here.
admin.site.register(Feed_Post)
admin.site.register(Comment)
# admin.site.register(Comment_User)

#superuser id:admin pw:1234
#민혁님 계정 id:MinHyeok pw:mh12341234