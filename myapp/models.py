from pydoc import describe
from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):   #для строкового представления объекта
        return self.title

    class Meta:
        ordering = ['complete'] 
