# Generated by Django 4.2.4 on 2024-03-01 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_comment_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cars.car'),
        ),
    ]
