from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey('Question')
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')

  def popular(self):
    return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(User, related_name='question_like_user')
