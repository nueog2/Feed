
from .models import Feed_Post, Comment, Artist_Post, Artist_Comment
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializer import Feed_PostSerializer, CommentSerializer , Artist_PostSerializer, Artist_CommentSerializer
from django.db import models 
from rest_framework.response import Response


class Feed_PostList(ListCreateAPIView):
    queryset = Feed_Post.objects.all()
    serializer_class = Feed_PostSerializer

class Feed_PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Feed_Post.objects.all()
    serializer_class = Feed_PostSerializer




class CommentPostList(ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)

class ClickLikeAPIView(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        post = Feed_Post.objects.get(id=post_id)
        post.like = not post.like
        post.save()
        return Response({'message': post.like})


class ArtistCommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(user_id=2)


class Artist_PostList(ListCreateAPIView):
    queryset = Artist_Post.objects.all()
    serializer_class = Artist_PostSerializer

class Artist_PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Artist_Post.objects.all()
    serializer_class = Artist_PostSerializer

class Artist_CommentPostList(ListCreateAPIView):
    serializer_class = Artist_CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Artist_Comment.objects.filter(post=post_id)
    
class Artist_ClickLikeAPIView(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        post = Artist_Post.objects.get(id=post_id)
        post.like = not post.like
        post.save()
        return Response({'message': post.like})



    
# #1. 댓글에 유저정보를 저장할 공간을 (필드 )만들기
# #2. manytomanyfield 사용 
# #3. POST클릭해서 받는 댓글에 manytomanyfield 추가해주기
# #4. 댓글에 유저정보를 저장하기 위해 댓글을 저장하는 시점에 유저정보를 저장해주기