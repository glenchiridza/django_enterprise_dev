# Generated by Django 3.0.8 on 2023-01-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_3', '0004_auto_20230107_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='engine2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, null=True, verbose_name='Engine')),
            ],
            options={
                'db_table': 'chapter3_practice_engine',
            },
        ),
    ]
