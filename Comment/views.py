from django.shortcuts import render , redirect
from .models import FeedComment
# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.http import JsonResponse

# Create your views here.

def Feed_Comment(request):

    if request.method == "POST":
        content = request.POST.get('content')
        comment = FeedComment.objects.create(content=content)
        comment.save()
        return redirect('feed')
    else:
        comments = FeedComment.objects.all()
        context = {"comments": comments}
        return render(request, 'feed.html', context=context)
    # 
    # posts = Post.objects.all()
    # context = {"posts" : posts}
    # return render(request, 'feed.html' , context = context)

# #좋아요기능
# @csrf_exempt 
# def like_ajax(request):
#     req = json.loads(request.body) 
#     pk = req['id'] 

#     comment = Feed_Comment.objects.get(id = pk)

#     if comment.already_like == True: #좋아요가 눌러져있으면
#         comment.already_like = False
#         status = comment.already_like
#         comment.like = '<i class="far fa-heart"></i> '
#         message = "좋아요 취소"
#     else: #좋아요가 안눌러져있으면
#         comment.already_like = True
#         status = comment.already_like
#         comment.like = ' <i class="fas fa-heart" style="color:red"></i>'
#         message = "좋아요"
#     comment.save()

#     return JsonResponse({'id': pk, 'message': message, 'status':status})