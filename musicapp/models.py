from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    plays = models.IntegerField()
    duration = models.IntegerField()
    file = models.FileField(upload_to='songs/')

    class Meta:
        db_table = 'songs'

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'artists'

    def __str__(self):
        return self.name
