from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    memo = models.TextField(max_length=1024)

    def __str__(self):
        return self.title
    