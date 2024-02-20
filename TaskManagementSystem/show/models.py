from django.db import models
from category.models import Category

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    # task = models.ForeignKey(Show , on_delete=models.CASCADE)

    def __str__(self):
        return self.title