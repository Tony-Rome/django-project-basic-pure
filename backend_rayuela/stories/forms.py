from django import forms
from .models import Story, Hashtag


class StoryCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(StoryCreateForm, self).__init__(*args, **kwargs)
        print(self.user.email)
        self.fields['writer'].initial = self.user

    writer = forms.CharField(label="Writer", disabled=True, widget=forms.TextInput())

    class Meta:
        model = Story
        fields = '__all__'
        exclude = ('writer',)
        widgets = {
            'body': forms.Textarea(attrs={'row': 30, 'col': 30})
        }

    def save(self, commit=True):
        story = super().save(commit=False)
        story.writer = self.user
        if commit:
            story.save()
            self.split_tag(story=story)

    def split_tag(self, story):
        tags = self.cleaned_data.get('tags')
        print("TAGS: ", tags)
        splited_tags = tags.split(" ")
        print("SPLIT:", splited_tags)
        try:
            for hashtag in splited_tags:
                hashtag_model = Hashtag(story=story, hashtag=hashtag)
                hashtag_model.save()
            print("SE GUARDARON LOS HASHTAGS")
        except:
            raise ValueError



