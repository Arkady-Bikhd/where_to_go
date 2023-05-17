from django.db import models

# Create your models here.

class Place(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    description_short = models.CharField(max_length=350, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')


    def __str__(self):
        return self.title
    
class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, verbose_name='фотография')
    image_number = models.IntegerField(blank=True, verbose_name='Номер картинки')

    def __str__(self):
        return f'{self.image_number} {self.place}'