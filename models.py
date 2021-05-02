from django.db import models

# Create your models here.


class Genre(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """ The Model to hold a list of Movies """
    name = models.CharField(max_length=250)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    stars = models.FloatField(default=1.0)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


