from django.shortcuts import render, redirect
from .forms import HopscotchCreateForm
from .models import Hopscotch, HopscotchAndStory
from django.db.models import Count

def hopscotch_home(request, *args, **kwargs):
    '''
        La base de datos sqlite no soporta .distinct() con parametros.
        Para consultas más refinadas se recomienda ocupar POSTGRESQL.

        TODO
            Encontrar una queryset que me permita obtener:
                Cantidad de historias de un cierto hopscotch que pertenece a un cierto usuario.
                - Flujo de ejemplo:
                    - Obtener usuario (request.user)
                    - Filtrar hopscotch por usuario (writer=request.user)
                    - Agregar a cada hopscotch un campo que contenga
                      la cantidad total de historias que están relacionadas.

    '''

    hopscotchs = Hopscotch.objects.filter(writer=request.user)

#    response = Hopscotch.objects.filter(writer=request.user).annotate(count_stories=(

#    ))
#    print("RESPONSE:", response)

#    test = Hopscotch.objects.filter(writer=request.user).first()
#    print("TEST:", test)
#    count = HopscotchAndStory.objects.filter(hopscotch=test).values('story').count()
#    print("COUNT: ", count)
#    numbers_stories = [
#        HopscotchAndStory.objects.filter(hopscotch=hopscotch).count()
#        for hopscotch in hopscotchs
#        ]
#    print("TIPO: ",type(numbers_stories))
#    print("NUMBERS: ", numbers_stories)
    data = {
        "hopscotchs": hopscotchs,
 #       "numbers": numbers_stories
    }
    return render(request, "pages/hopscotch.html", context=data)


def hopscotch_create(request, *args, **kwargs):
    if request.method == "POST":
        form = HopscotchCreateForm(request.POST or None, user=request.user)

        if form.is_valid():
            form.save()
            return redirect("hopscotch-urls:hopscotch-home")
        else:
            data = {"form": form}
            return render(request, "pages/hopscotch.html", context=data)


def hopscotch_update():
    pass

def hopscotch_delete():
    pass

def hopscotch_get():
    pass

def hoptscotch_get_list():
    pass