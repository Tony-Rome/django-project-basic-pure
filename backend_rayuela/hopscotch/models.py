from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from storie_routes import StoryRoute
# from accounts import models
# Create your models here.


class HopscotchAndStory(models.Model):
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE)
    hopscotch = models.ForeignKey("Hopscotch", on_delete=models.CASCADE)


class Hopscotch(models.Model):
    title = models.CharField(max_length=30)
    story = models.ManyToManyField("stories.Story", through=HopscotchAndStory)
    state = models.BooleanField(default=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Se agrego post-modelo

    class Meta:
        permissions = (
            ("can_be_admin", "Can be admin"),
        )

    def __str__(self):
        return f"{self.id} {self.title}"

    @property
    def get_all(self):
        return f"Autor: {self.writer}\n Story: {self.story}\n State: {self.state}"



