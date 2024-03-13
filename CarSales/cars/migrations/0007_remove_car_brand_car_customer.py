# Generated by Django 4.2.4 on 2024-03-13 13:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0006_car_category_delete_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.AddField(
            model_name='car',
            name='customer',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
