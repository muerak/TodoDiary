from django.db import models
from datetime import datetime

# Create your models here.
class MyTodo(models.Model) :
    list = models.CharField(max_length=150)
    #diary = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False)
    remove = models.BooleanField(default=False)

    def __str__(self):
        return self.list

