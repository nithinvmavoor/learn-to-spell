import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #constructor
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    #was_published_recently.admin_order_field = 'pub_date' 
    was_published_recently.boolean = True #display tick and cross images for boolean True and False
    was_published_recently.short_description = 'Published recently?' #change title in listing page

    question_text.short_description = 'Question'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #constructor
    def __str__(self):
        return self.choice_text