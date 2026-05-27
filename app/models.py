from django.db import models


class Game(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    genre = models.CharField(max_length=50)

    release_year = models.IntegerField()

    rating = models.FloatField()

    is_cart = models.BooleanField(default=False)

    def __str__(self):
        return self.title