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
        return QuestionModel.objects.create(
            author_id=self._user.id,
            title=self.cleaned_data.get('title'),
            text=self.cleaned_data.get('text')
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
        return AnswerModel.objects.create(
            author_id=self._user.id,
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question']
        )
    

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
        }
    ))  
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
                'placeholder': 'Password'
            }
    ))

    def save(self):
        cd = self.cleaned_data
        return User.objects.create_user(
            username=cd.get('username'),
            password=cd.get('password'),
            email=cd.get('email')
        )


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
            attrs={
                'placeholder': 'Username'
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
                'placeholder': 'Password'
            }
    ))
