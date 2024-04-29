# Generated by Django 5.0.4 on 2024-04-29 18:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('muscle_group', models.CharField(choices=[('CH', 'Chest'), ('SH', 'Shoulder'), ('UB', 'Upper Back'), ('LB', 'Lower Back'), ('LE', 'Legs'), ('CA', 'Calf'), ('BI', 'Biceps'), ('TR', 'Triceps'), ('AB', 'Abs')])),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('exercise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.exercisetype')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField(verbose_name='Workout Date')),
                ('notes', models.TextField(max_length=250)),
                ('exercises', models.ManyToManyField(to='main_app.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
