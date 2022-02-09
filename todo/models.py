from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

  class Status(models.TextChoices):
    ON_GOING = 'OnGoing'
    NOT_STARTED = 'NotStarted'
    COMPLETED = 'Completed'

  title = models.CharField(max_length=100)
  memo = models.TextField(blank=True)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  status = models.CharField(max_length=10, choices=Status.choices, default=Status.NOT_STARTED)

  def __str__(self):
    return f'{self.title} - owner: {self.user.username}'


class TodoUser(User):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"email={self.email}"


  