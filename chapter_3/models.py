from django.db import models

YESNO_CHOICES = (
    (True,'Yes'),
    (False,'No'),
)


class Vehicle(models.Model):
    vin = models.CharField(
        verbose_name='VIN',
        max_length=75,
        unique=True,
        blank=True,
        null=True,
    )
    sold = models.BooleanField(
        verbose_name='Sold?',
        choices=YESNO_CHOICES,
        default=False,
        blank=True,
        null=True,
    )


class VehicleModel(models.Model):
    name = models.CharField(
        verbose_name='Model',
        max_length=75,
        unique=True,
        blank=True,
        null=True,
    )


class Engine(models.Model):
    name = models.CharField(
        verbose_name='Engine',
        max_length=75,
        blank=True,
        null=True,
    )