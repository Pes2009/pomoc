from django.db import models

# Create your models here.

class Ziom(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ziomka(models.Model):
    album = models.ManyToManyField(Ziom, related_name='zioms')
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Words(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

class Categories(models.Model):
    name = models.CharField(max_length=100)
    words = models.ManyToManyField(Words, related_name='words')

    def __str__(self):
        return self.name
