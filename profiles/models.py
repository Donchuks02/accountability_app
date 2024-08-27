from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    currently_learning = models.CharField(max_length=50, blank=True)
    github_profile_address = models.CharField(max_length=200)
    progress = models.FloatField(default=0)
    last_submission = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.user.username})"




class FormModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forms')

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question} ({self.answer})"