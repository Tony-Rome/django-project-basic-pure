from django.contrib import admin
from .models import ColaboratorAndStoryRouter, ColaboratorAndHopscotch, Comment, Colaborator, Like


admin.site.register(Colaborator)
admin.site.register(Comment)
admin.site.register(ColaboratorAndHopscotch)
#admin.site.register(Writer)
admin.site.register(Like)
admin.site.register(ColaboratorAndStoryRouter)

