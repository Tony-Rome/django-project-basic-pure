from django.urls import path
from .views import story_home ,story_list, story_create, story_delete, story_detail, story_update, all_stories

app_name = 'stories-urls'

urlpatterns = [
    path('home/', story_home, name='story-home'),
    path('create/', story_create, name='story-create'),
    path('list/', story_list, name='story-list'),
    path('story/', story_detail, name='story-detail'),
    path('update/', story_update, name='story-update'),
    path('delete/', story_delete, name='story-delete'),
    path('all-stories', all_stories, name='all-stories')
]
