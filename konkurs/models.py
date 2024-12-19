from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Competition(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    min_age = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    max_age = models.PositiveIntegerField(default=0, validators=[MinValueValidator(2)])
    min_point = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    max_point = models.PositiveIntegerField(default=0, validators=[MinValueValidator(2)])
    image = models.ImageField(upload_to='competition/')

    def __str__(self):
        return f'{self.name}'
