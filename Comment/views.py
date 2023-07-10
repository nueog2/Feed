
from .models import Feed_Post, Comment #, #Comment_User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import APIView
from .serializer import Feed_PostSerializer, CommentSerializer
from django.db import models 

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

# class ClickLikeAPIView(APIView):
#     def post(self, request):
#         post_id = request.data.get('post_id')
#         post = Feed_Post.objects.get(id=post_id)
#         post.like = not post.like
#         post.save()
#         return Response({'message': 'ok'})


# class ArtistCommentList(ListCreateAPIView):
#     queryset = Comment_User.objects.filter(id=2).values('user_id')


    
# #1. 댓글에 유저정보를 저장할 공간을 (필드 )만들기
# #2. manytomanyfield 사용 
# #3. POST클릭해서 받는 댓글에 manytomanyfield 추가해주기
# #4. 댓글에 유저정보를 저장하기 위해 댓글을 저장하는 시점에 유저정보를 저장해주기