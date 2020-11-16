from django.urls import path
from .views import stories_routes_home, stories_routes_create, all_comments
app_name = 'stories-routes-urls'

urlpatterns=[
    path('home/', stories_routes_home, name='stories-routes-home'),
    path('create/', stories_routes_create, name='stories-routes-create'),
    path('all-comments/', all_comments, name='stories-routes-comments'),
]