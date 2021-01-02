from django import forms

from talk.models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'row': 5, 'placeholder': '输入内容'}
        ),
        max_length=4000,
        help_text='文本最大长度4000'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
