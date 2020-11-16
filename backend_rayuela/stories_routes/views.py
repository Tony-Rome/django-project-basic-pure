from django.shortcuts import render, redirect
from .forms import StoryRouteCreateForm
from .models import StoryRoute
from writers.models import Comment
# Create your views here.


def stories_routes_home(request):
    stories_routes = StoryRoute.objects.filter(writer=request.user)
    data = {"stories_routes": stories_routes}
    return render(request, "pages/stories_routes.html", context=data)


def stories_routes_create(request):
    if request.method == "POST":
        form = StoryRouteCreateForm(request.POST or None, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('stories-routes-urls:stories-routes-home')

        else:
            data = {"form": form}
            return render(request, "pages/stories_routes.html", context=data)

    return redirect('stories-routes-urls:stories-routes-home')


def all_comments(request):
    print("POST: ",request.POST['comments'])
    id_story_route = request.POST['comments']
    print(id_story_route)
    comments = 1
    data = {"comments": comments}
    return render(request, "pages/stories_routes.html", context=data)