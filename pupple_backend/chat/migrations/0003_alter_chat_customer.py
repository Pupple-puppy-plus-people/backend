# Generated by Django 3.2 on 2022-05-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='customer',
            field=models.IntegerField(),
        ),
    ]
