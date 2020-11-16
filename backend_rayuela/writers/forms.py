from django import forms
from .models import Comment
from stories_routes.models import StoryRoute


class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.id_story_route = kwargs.pop('id_story_route')
        super(CommentCreateForm, self).__init__(*args, **kwargs)
        self.fields['writer'].initial = self.user
        self.fields['story_route'].initial = self.id_story_route

    writer = forms.CharField(disabled=True)
    story_route = forms.CharField(disabled=True)

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'row': 30, 'col': 30, 'style': 'border-color: black; border-radius: 10px'})
        }
        labels = {
            "content": "Postea tu comentario.",
        }

    def save(self, *args, **kwargs):
        comment = super().save(commit=False)
        comment.writer = self.user
        print("RESULTADO STORYROUTE; ", StoryRoute.objects.get(id=self.id_story_route))
        comment.story_route = StoryRoute.objects.get(id=self.id_story_route)
        try:
            comment.save()
        except:
            raise ValueError

    def save_reply(self, *args, **kwargs):
        print(kwargs)
        id_reply = kwargs.pop('id_reply')
        comment = super().save(commit=False)
        comment.reply = Comment.objects.get(id=id_reply)
        try:
            comment.save()
            print("COMMENTSAVE: ", comment)
        except:
            raise ValueError


