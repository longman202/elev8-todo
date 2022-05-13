import email
from optparse import Option
from ssl import Options
from unicodedata import category
from django.db import models

# Create your models here.
category_choices = (
    ("hard", "Hard"),
    ("medium", "Medium"),
    ("easy", "Easy"),
)
class Task(models.Model):
    '''Creating a task table in database'''
    name = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=category_choices)
    description = models.CharField(max_length=400, blank=True, verbose_name='Describe your task', null=True)

    def __str__(self):
        return self.name
        

    class Meta:
        ordering = ['-id']
