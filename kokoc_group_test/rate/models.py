from django.db import models


class Valute(models.Model):
    
    name = models.CharField(max_length=200)
    charcode = models.CharField(max_length=3)
    rate = models.FloatField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
    
    def __str__(self):
        return self.name
    