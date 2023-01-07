# Generated by Django 3.0.8 on 2023-01-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='vehicle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_engine', to='chapter_3.VehicleModel', verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engine_vehicle', to='chapter_3.Engine', verbose_name='engine'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_vehicle', to='chapter_3.VehicleModel', verbose_name='Model'),
        ),
    ]
