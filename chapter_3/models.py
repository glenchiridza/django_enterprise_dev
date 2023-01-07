from django.db import models
from django.db.models.functions import Lower

YESNO_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
)

MAKE_CHOICES = (
    (1, 'Buick'),
    (2, 'Cadillac'),
    (3, 'Chevrolet'),
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
    make = models.PositiveIntegerField(
        choices=MAKE_CHOICES,
        verbose_name='Vehicle Make/Brand',
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

    def __str__(self):
        MAKE_CHOICES_DICT = dict(MAKE_CHOICES)
        return MAKE_CHOICES_DICT[self.make] + ' ' + self.vehicle_model.name


class VehicleModel(models.Model):
    name = models.CharField(
        verbose_name='Model',
        max_length=75,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Vehicle Model'
        verbose_name_plural = 'Vehicle Models'

        # ordering = ['name', 'someotherfield'] ascending order
        ordering = ['-name']  # descending order

        indexes = [
            models.Index(fields=['name']),
            models.Index(
                fields=['-name'],
                name='desc_name_idx'
            ),
            # models.Index(
            #     Lower('name').desc(),
            #     name='lower_name_idx'
            # )
            models.Index(
                fields=['-name'.lower()],
                name='lower_name_idx'
            )

        ]


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


# for side practice we use the engine2 in lowercase model
class engine2(models.Model):
    name = models.CharField(
        verbose_name='Engine',
        max_length=75,
        blank=True,
        null=True
    )

    # using db_table to explicitly specify the db_table of engine2
    # by default it would be {{app_name}}_{{model_name}}
    class Meta:
        db_table = 'chapter3_practice_engine'
