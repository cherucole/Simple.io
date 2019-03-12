from django.db import models
from datetime import datetime


class Item(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
