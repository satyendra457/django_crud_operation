from django.db import models

# Create your models here..
class BookList(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    author = models.CharField(max_length=150)
    about = models.TextField(max_length=500)

    def __str__(self):
        return self.title

