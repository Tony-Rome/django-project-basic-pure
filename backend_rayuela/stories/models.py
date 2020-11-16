from django.db import models
from django.conf import settings


class Story(models.Model):
 #   hopscotch = models.ManyToManyField(Hopscotch)
 #   story_route = models.ManyToManyField(StoryRoute)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=1024)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Author solamente puede ser uno solo
#    likes = models.CharField()  # puede tener muchos likes de muchos usuarios relacion manyToMany, no se si es necesario este campo
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, unique=True, null=True, blank=True)
#    image = models.FileField(upload_to="/images", blank=True, null=True)

    def __str__(self):
      return f"Titulo: {self.title} - contenido: {self.body}"


class Hashtag(models.Model):

   story = models.ForeignKey(Story, on_delete=models.CASCADE)
   hashtag = models.CharField(max_length=30)
   timestamp = models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return f"{self.story.id} - {self.hashtag} - {self.timestamp}"
