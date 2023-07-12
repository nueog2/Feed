from rest_framework import serializers

from .models import Feed_Post, Comment , Artist_Post, Artist_Comment#, Comment_User

class Feed_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class Artist_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist_Post
        fields = '__all__'

class Artist_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist_Comment
        fields = '__all__'

# class Comment_UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment_User
#         fields = '__all__'