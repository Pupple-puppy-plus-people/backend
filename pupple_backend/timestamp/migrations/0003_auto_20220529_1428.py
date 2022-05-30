# Generated by Django 3.2 on 2022-05-29 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogs', '0002_auto_20220524_1520'),
        ('timestamp', '0002_alter_timestamp_press_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timestamp',
            old_name='elapsed_time',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='timestamp',
            name='userdog',
        ),
        migrations.AddField(
            model_name='timestamp',
            name='dog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='timestamp', to='dogs.dog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timestamp',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='timestamp', to='users.user'),
            preserve_default=False,
        ),
    ]