from django.db import models

# Create your models here.
CHOICE = (('danger', 'high'), ('warning', "normal"), ('primary', 'low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    memo = models.TextField(max_length=1024)
    priority = models.CharField(max_length=50, choices=CHOICE)

    due_date = models.DateField()

    def __str__(self):
        return self.title
    