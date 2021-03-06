from django.db import models
import random
# Create your models here.
DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    number_of_ques=models.IntegerField()
    time=models.IntegerField()
    required_score=models.IntegerField()
    difficulty=models.CharField(max_length=100,choices=DIFF_CHOICES)
    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions=list(self.question_set.all())
        random.shuffle(questions)
        return questions

    class Meta:
        verbose_name_plural = 'Quizes'

