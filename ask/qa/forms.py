from django import forms
from .models import Question as QuestionModel, Answer as AnswerModel
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Question title '}))
    text = forms.CharField(
        label="Question", 
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Question',
                'style':'width:100%; resize: none;'
            }
        )
    )

    def save(self):
        author = User.objects.get_or_create(username='test_user')[0] # remove later
        return QuestionModel.objects.create(
            author_id=author.id,
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text']
        )   

class AnswerForm(forms.Form):
    text = forms.CharField(
        label="Answer", 
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Answer',
                'style':'width:100%; resize: none;',
                'rows':'5'
            }
        )
    )
    question = forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        author = User.objects.get_or_create(username='test_user')[0] # remove later
        return AnswerModel.objects.create(
            author_id=author.id,
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question']
        )
    