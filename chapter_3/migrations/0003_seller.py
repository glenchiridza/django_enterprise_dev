# Generated by Django 3.0.8 on 2023-01-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_3', '0002_auto_20230107_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Seller Name')),
                ('vehicle', models.ManyToManyField(blank=True, related_name='vehicle_sellers', related_query_name='vehicle_seller', to='chapter_3.Vehicle', verbose_name='Vehicles')),
            ],
        ),
    ]