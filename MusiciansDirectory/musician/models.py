from django.db import models
from album.models import Album

# Create your models here.
class Musician(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phn_num = models.CharField(max_length=255)
    instrument = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
