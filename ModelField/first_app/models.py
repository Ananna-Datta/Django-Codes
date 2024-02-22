from django.db import models

# Create your models here.
class Mymodel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    float_field = models.FloatField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    # null_boolean_field = models.NullBooleanField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()

    
