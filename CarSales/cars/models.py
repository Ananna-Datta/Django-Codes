from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"
    
