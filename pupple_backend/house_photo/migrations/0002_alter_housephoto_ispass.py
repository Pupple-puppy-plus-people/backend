# Generated by Django 3.2 on 2022-05-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housephoto',
            name='ispass',
            field=models.BooleanField(default=False),
        ),
    ]
