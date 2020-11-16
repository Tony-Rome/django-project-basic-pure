from django.urls import path
from .views import all_comments, create_comment, create_reply_comment, all_comments_tree

app_name='writers-urls'

urlpatterns = [
    path('all-comments/', all_comments, name='all-comments'),
    path('create/', create_comment, name='create-comment'),
    path('create-reply-comment/', create_reply_comment, name='create-reply-comment'),
    path('all-comments-tree/', all_comments_tree, name='all-comments-tree')
]