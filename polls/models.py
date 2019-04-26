
# Create your models here.
from django.db import models
from django.utils import timezone

class Question(models.Model):
    id=models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_answer=models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question