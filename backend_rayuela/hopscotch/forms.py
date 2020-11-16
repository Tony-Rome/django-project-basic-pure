from django import forms
from .models import Hopscotch, HopscotchAndStory
from stories.models import Story

class HopscotchCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.stories_list = tuple([(story.id, story.title) for story in Story.objects.filter(writer=self.user)])
        super(HopscotchCreateForm, self).__init__(*args, **kwargs)
        self.fields['writer'].initial = self.user
        self.fields['stories'] = forms.MultipleChoiceField(
            label="Elige tus historias",
            widget=forms.CheckboxSelectMultiple, choices=self.stories_list)

    writer = forms.CharField(disabled=True)

    class Meta:
        model = Hopscotch
        fields = '__all__'
        exclude = ('story','writer',)
        labels = {
            "state": "Estado de tu rayuela (Pública o privada)",
        }

    def save(self):
        hopscotch = super().save(commit=False)
        hopscotch.writer = self.user  # dueño de hopscotch
        stories = self.cleaned_data.get('stories')
        hopscotch.save()
        self.save_stories(stories=stories, hopscotch=hopscotch)

    def save_stories(self, stories, hopscotch):
        try:
            for id_story in stories:
                story = Story.objects.get(id=int(id_story))
                added_story = HopscotchAndStory(story=story, hopscotch=hopscotch)
                added_story.save()
        except:
            raise ValueError


