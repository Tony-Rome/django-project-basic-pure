from django.db import models
from django.conf import settings


class Comment(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    reply = models.ForeignKey("self", null=True, on_delete=models.CASCADE, blank=True)  # Respuesta
    content = models.CharField(max_length=255)  # comentario
    story = models.OneToOneField("stories.Story", on_delete=models.CASCADE, null=True, blank=True)
    story_route = models.OneToOneField("stories_routes.StoryRoute", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return f"Comentario id:{self.id} - comentario padre-id: {self.reply}"


class Like(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_event = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

'''
class Writer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=40)
'''


class ColaboratorAndHopscotch(models.Model):
    hopscotch = models.ForeignKey("hopscotch.Hopscotch", on_delete=models.CASCADE)
    colaborator = models.ForeignKey("Colaborator", on_delete=models.CASCADE)


class ColaboratorAndStoryRouter(models.Model):
    story_route = models.ForeignKey("stories_routes.StoryRoute", on_delete=models.CASCADE)
    colaborator = models.ForeignKey("Colaborator", on_delete=models.CASCADE)


class Colaborator(models.Model):
    hopscotch = models.ManyToManyField("hopscotch.Hopscotch", through=ColaboratorAndHopscotch)
    story_route = models.ManyToManyField("stories_routes.StoryRoute", through=ColaboratorAndStoryRouter)
    writer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
