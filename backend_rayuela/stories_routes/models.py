from django.db import models
from django.conf import settings

class StoryRoute(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE)
#    colaborator = models.ManyToManyField(Colaborator)
#   title = models.CharField()

    def __str__(self):
        return f"ID: {self.id}\n STORIES: ROUTE: {self.story}"



class RouteOrder(models.Model):
    story_route = models.ForeignKey(StoryRoute, on_delete=models.CASCADE)
    story_parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)  # valores positivos
    story_id = models.IntegerField()  # UID de Story


