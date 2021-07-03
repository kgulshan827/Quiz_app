from django.db import models
from Quizzes.models import Quiz
from django.contrib.auth.models import User

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)