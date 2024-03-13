from django.db import models
# from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=255)
    # musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(null=True)
    rating = models.IntegerField()
    # rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.album_name
