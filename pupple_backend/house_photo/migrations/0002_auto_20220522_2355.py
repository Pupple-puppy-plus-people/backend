# Generated by Django 3.2 on 2022-05-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='housephoto',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housephoto',
            name='ispass',
            field=models.BooleanField(default=False),
        ),
    ]
