from django.db import models

# Create your models here.

class Serie(models.Model):
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOISE = (
        (HORROR,'HORROR'),
        (COMEDY,'COMEDY'),
        (ACTION,'ACCION'),
        (DRAMA,'DRAMA')
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=100,choices=CATEGORIES_CHOISE)

    def __str__(self):
        return self.name