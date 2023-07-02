from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    description_short = models.CharField(max_length=350, verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Описание')

    class Meta:
        ordering = ['id']        
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title
    

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, verbose_name='фотография')
    image_number = models.IntegerField(default=0, verbose_name='Номер картинки')

    class Meta:
        ordering = ['place']
        
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return f'{self.image_number} {self.place}'
    