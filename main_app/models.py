from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Volume(models.Model):
    def __str__(self):
        return str(self.id)  

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.title.encode('utf-8'))


class Exercise(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    difficulty_level = models.IntegerField(default=0, validators=[MinValueValidator(1),
       MaxValueValidator(10)])
    def __str__(self):
        return str(self.id)


class Solution(models.Model):
    excercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    def __str__(self):
        return str(self.id)
