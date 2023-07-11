from .views import Feed_PostList, Feed_PostDetail, CommentPostList ,ArtistCommentList,ClickLikeAPIView
from django.urls import path


urlpatterns = [
    path('',Feed_PostList.as_view()),
    path('detail/<int:pk>/',Feed_PostDetail.as_view()),
    path('detail/<int:post_id>/comment/',CommentPostList.as_view()),
    path('like/',ClickLikeAPIView.as_view()),
    path('artist/',ArtistCommentList.as_view()),
]