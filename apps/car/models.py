from django.db import models

from apps.model.models import modelo
from apps.user.models import User


class Car(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Número')
    plate = models.CharField(max_length=10),
    mileage = models.FloatField(max_length=30),
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    model = models.ForeignKey(modelo, on_delete=models.CASCADE,
                              null=True),

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return '%s (%s)' % (self.number, self.plate)
