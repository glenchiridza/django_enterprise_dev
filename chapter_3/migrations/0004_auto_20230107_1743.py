# Generated by Django 3.0.8 on 2023-01-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_3', '0003_seller'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={'ordering': ['-name'], 'verbose_name': 'Vehicle Model', 'verbose_name_plural': 'Vehicle Models'},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='make',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Buick'), (2, 'Cadillac'), (3, 'Chevrolet')], null=True, verbose_name='Vehicle Make/Brand'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['name'], name='chapter_3_v_name_7ccb3d_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['-name'], name='desc_name_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['-name'], name='lower_name_idx'),
        ),
    ]
