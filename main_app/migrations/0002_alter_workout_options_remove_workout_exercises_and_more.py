# Generated by Django 5.0.4 on 2024-04-30 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='workout',
            name='exercises',
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main_app.workout'),
            preserve_default=False,
        ),
    ]
