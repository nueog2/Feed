from .views import Feed_PostList, Feed_PostDetail, CommentPostList ,ArtistCommentList,ClickLikeAPIView, Artist_PostList, Artist_PostDetail, Artist_CommentPostList, Artist_ClickLikeAPIView
from django.urls import path
from django.urls import path


urlpatterns = [
    path('',Feed_PostList.as_view()),
    path('detail/<int:pk>/',Feed_PostDetail.as_view()),
    path('detail/<int:post_id>/comment/',CommentPostList.as_view()),
    path('like/',ClickLikeAPIView.as_view()),
    path('artistcomment/',ArtistCommentList.as_view()),
    path('artist/',Artist_PostList.as_view()),
    path('artist/<int:pk>/',Artist_PostDetail.as_view()),
    path('artist/<int:post_id>/comment/',Artist_CommentPostList.as_view()),
    path('artistlike/', Artist_ClickLikeAPIView.as_view()),
]