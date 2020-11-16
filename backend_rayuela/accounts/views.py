import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.contrib.sessions.backends.cache import SessionStore
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Writer
from .forms import WriterCreationForm, WriterLoginForm

def writer_home(request):
    return render(request, "pages/home.html", context={})


def writer_profile(request, *args, **kwargs):
    return render(request, "pages/profile.html", context={})


@csrf_exempt
def login_writer(request, *args, **kwargs):
    #print(Writer.objects.all())
    if request.method == "POST":  # Si es válido
        print(request)
        email = request.POST['email']
        password = request.POST['password']
        writer = authenticate(email=email, password=password)
        print(writer)
        if writer is not None:
            login(request, writer)
            return redirect("accounts-urls:writer-home")

    form = WriterLoginForm()
    data = {"form" : form}
    return render(request, "pages/login.html", context=data)


@csrf_exempt
def logout_writer(request, *args, **kawrgs):
    print(request.user)
    logout(request)
    return render(request, "pages/preview.html", context={})


def create_user(request, *args, **kwargs):

    if request.method == "POST":
        writer_form = WriterCreationForm(request.POST)
        print(writer_form)
        print(writer_form.is_valid())
        if writer_form.is_valid():
            writer_form.clean_password2()
            writer_form.save()
            return redirect('accounts-urls:login')
        else:
            return redirect('accounts-urls:create-user')

        print("TODOS LOS WRITERS", Writer.objects.all())

    form = WriterCreationForm()
    data = {
        "form": form
    }
    return render(request, "pages/register.html", context=data)
#    return JsonResponse("Sin formulario", status=200)


@csrf_exempt
def view_profile(request, *args, **kwargs):
    if not request.user:
        return JsonResponse({"RESPONSE":"NO USER"},status=200)
    print(request.user)
    return JsonResponse({"RESPONSE":"OK"}, status=200)

