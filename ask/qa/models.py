from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='question_like_user')

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey('Question')
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')

  def popular(self):
    return self.order_by('-rating')
