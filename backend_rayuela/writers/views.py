from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Comment
from stories_routes.models import StoryRoute
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentCreateForm

print("ALL COMMENTS: ", Comment.objects.all())

def all_comments(request, *args, **kwargs):
    id_story_route = int(request.POST['comments'])
    story_route = StoryRoute.objects.get(id=id_story_route)
    comments = Comment.objects.filter(story_route=id_story_route)
    form = CommentCreateForm(user=request.user, id_story_route=id_story_route)
    data = {
        "comments": comments,
        "story_route": story_route,
        "id_story_route": id_story_route,
        "form": form
    }
    return render(request, 'pages/comments.html', context=data)


def create_comment(request, *args, **kwargs):
    if request.method == "POST":
        id_story_route = int(request.POST['id'])
        form = CommentCreateForm(request.POST or None, user=request.user, id_story_route=id_story_route)
        if form.is_valid():
            form.save()
        return redirect("stories-routes-urls:stories-routes-home")


def create_reply_comment(request):
    if request.method == "POST":
        id_story_route = int(request.POST['id_story_route'])
        id_reply = int(request.POST['id_reply'])
        form = CommentCreateForm(request.POST or None, user=request.user, id_story_route=id_story_route)
        if form.is_valid():
            print("ES VALIDO FORM")
            form.save_reply(id_reply=id_reply)
        else:
            print("NO ES VALIDO")
        return redirect("stories-routes-urls:stories-routes-home")


def all_comments_tree(request, *args, **kwargs):
    if request.method == "POST":
        return render(request, 'pages/main_comments.html', context={})