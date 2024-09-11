from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.app.name}'
