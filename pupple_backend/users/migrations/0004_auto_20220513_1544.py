# Generated by Django 3.2 on 2022-05-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220507_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='agreement',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='survey',
            field=models.IntegerField(default=0),
        ),
    ]
