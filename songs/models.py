from django.db import models
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nome")
    
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nome")
    artist = models.ForeignKey(Artist, on_delete= models.CASCADE, verbose_name="Artista")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{} ({})".format(self.name, self.artist.name)

