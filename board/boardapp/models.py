from django.db import models

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to="")
    good = models.IntegerField()
    read = models.IntegerField()
    read_text = models.TextField()