# Generated by Django 4.0.3 on 2022-03-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_remove_restaurant_location_restaurant_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
