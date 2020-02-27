from django.db import models


class Serie(models.Model):

    HORROR = 'horror'
    COMEDY = 'comedia'
    ACTION = 'accion'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedia'),
        (ACTION, 'Accion'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)