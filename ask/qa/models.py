from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(max_length=30)
    rating = models.IntegerField()
    author = User()
    likes = models.TextField(null=True) 

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey('Question')
    added_at = models.DateTimeField(max_length=30)
    author = User()

class QuestionManager(Question):
    def new():
        pass

    def popular():
        pass
    
