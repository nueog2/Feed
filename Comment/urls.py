from .views import Feed_PostList, Feed_PostDetail, CommentPostList #,ArtistCommentList
from django.urls import path


urlpatterns = [
    path('',Feed_PostList.as_view()),
    path('detail/<int:pk>/',Feed_PostDetail.as_view()),
    path('detail/<int:post_id>/comment/',CommentPostList.as_view()),
    # path('artist/',ClickLikeAPIView.as_view()),
    # path('',ArtistCommentList.as_view()),
]