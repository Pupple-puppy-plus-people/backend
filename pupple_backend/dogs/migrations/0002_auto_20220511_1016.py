# Generated by Django 3.2 on 2022-05-11 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='floor_auth',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='house_auth',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
