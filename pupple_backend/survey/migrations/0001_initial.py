# Generated by Django 3.2 on 2022-05-28 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dogs', '0004_merge_0002_auto_20220524_1520_0003_auto_20220522_2355'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('num_family', models.IntegerField()),
                ('family', models.TextField()),
                ('family_agree', models.BooleanField()),
                ('experience', models.BooleanField()),
                ('house_form', models.CharField(max_length=100)),
                ('noise_issue', models.TextField()),
                ('move_issue', models.TextField()),
                ('empty_issue', models.TextField()),
                ('family_issue', models.TextField()),
                ('neutering', models.BooleanField()),
                ('main_person', models.TextField()),
                ('vaccin_cost', models.TextField()),
                ('food_cost', models.TextField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='dogs.dog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_info', models.BooleanField(default=False, null=True)),
                ('location_info', models.BooleanField(default=False, null=True)),
                ('chit_penalty', models.BooleanField(default=False, null=True)),
                ('cannot_adopt', models.BooleanField(default=False, null=True)),
                ('more_info', models.BooleanField(default=False, null=True)),
                ('dog_entrance', models.BooleanField(default=False, null=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agreement', to='dogs.dog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agreement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
