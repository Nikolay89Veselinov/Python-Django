# Generated by Django 2.1.13 on 2021-01-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to='images/pets'),
        ),
    ]
