from django.shortcuts import render


def preview_page(request, *args, **kwargs):
    return render(request, "pages/preview.html", context={})


def login_page(request):
    print(request.user)
    return render(request, "pages/auth.html",context={})


def logout_page(request):
    print(request.user)
    return render(request, "pages/auh.html", context={})