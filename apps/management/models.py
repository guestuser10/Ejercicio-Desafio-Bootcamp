from django.db import models

from apps.car.models import Car


class Management(models.Model):
    mileage = models.FloatField(max_length=30, verbose_name='kilometraje'),
    description = models.TextField(max_length=500, verbose_name='descripcion'),
    cost = models.FloatField(max_length=20, verbose_name='costo'),
    date = models.DateField(verbose_name='fecha'),
    auto = models.ForeignKey(Car, on_delete=models.CASCADE,
                             null=True, verbose_name='modelo'),

    class Meta:
        verbose_name = 'mantenimiento'
        verbose_name_plural = 'mantenimientos'

    def __str__(self):
        return '%s (%s)' % (self.number, self.plate)
