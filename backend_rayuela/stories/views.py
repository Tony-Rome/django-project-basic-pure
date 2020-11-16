import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Story, Hashtag
from .forms import StoryCreateForm
# Create your views here.

@csrf_exempt
def story_home(request):
#    hashtags = Hashtag.objects.select_related('story__writer').filter(story__writer=Subquery)
    stories = Story.objects.filter(writer=request.user)
#    hastags = response[0].hashtag_set.all()
#    union = response.intersection(hastags)
#    print(response)
#    print(union)
#    user = stories.writer
#    print("STORIES:", stories)
#    print("uSER: ", user)
#    print(hashtags)
#    stories = [story for story in Story.objects.filter(writer=request.user)]
#    for story in stories:
#        total_stories = [hashtag for hashtag in Hashtag.objects.select_related('story').order_by('timestamp')]
#    total_stories = stories.hashtag_set.all()
#    print("TOTAL STORIES: ",total_stories)
#    hashtags = Hashtag.objects.get(story=)
#    print("STORIES: ", stories)
#    print(hashtags)
    data = {
        "stories": stories
    }
    return render(request, "pages/story.html", context=data)

@csrf_exempt
def story_list(request):
    story = Story.objects.all()
    print(story)
    for s in story:
        print(s.writer)
        print(s.timestamp)
    data = {}
    return JsonResponse(data, status=200)


def story_detail(request, *args, **kwargs):
    data = {}
    return JsonResponse(data, status=200)


def all_stories(request, *args, **kwargs):
    return render(request, "pages/story.l", context={})

@csrf_exempt
def story_create(request, *args, **kwargs):
    if request.method == "POST":
        form = StoryCreateForm(request.POST, user=request.user)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("stories-urls:story-home")
        else:
            data = {"form": form}
#    print(request.user.is_valid())
#    data = json.loads(request.body)
#    title = data['title']
#    body = data['body']
#    story = Story(title=title, body=body)
#    story.save()
    return render(request, "pages/story.html", context=data)


def story_update(request, *args, **kwargs):
    data = {}
    return JsonResponse(data, status=200)


def story_delete(request, *args, **kwargs):
    data = {}
    return JsonResponse(data, status=200)
