from django.db import models

YESNO_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
)


class Vehicle(models.Model):
    vehicle_model = models.ForeignKey(
        'VehicleModel',
        on_delete=models.CASCADE,
        verbose_name='Model',
        related_name='model_vehicle',
        blank=True,
        null=True
    )
    engine = models.ForeignKey(
        'Engine',
        on_delete=models.CASCADE,
        verbose_name='engine',
        related_name='engine_vehicle',
        blank=True,
        null=True
    )
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
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True)


class VehicleModel(models.Model):
    name = models.CharField(
        verbose_name='Model',
        max_length=75,
        unique=True,
        blank=True,
        null=True,
    )


class Engine(models.Model):
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete=models.CASCADE,
        verbose_name='Model',
        related_name='model_engine',
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name='Engine',
        max_length=75,
        blank=True,
        null=True,
    )


class Seller(models.Model):
    name = models.CharField(
        verbose_name='Seller Name',
        max_length=150,
        blank=True,
        null=True,
    )
    vehicle = models.ManyToManyField(
        Vehicle,
        verbose_name='Vehicles',
        related_name='vehicle_sellers',
        related_query_name='vehicle_seller',
        blank=True,
    )
