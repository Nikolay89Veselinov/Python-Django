# Generated by Django 2.2.28 on 2022-06-01 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0009_like_aa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='aa',
        ),
    ]
