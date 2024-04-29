from django.db import models
from django.contrib.auth.models import User

MUSCLE_GROUP = (
    ('CH', 'Chest'),
    ('SH', 'Shoulder'),
    ('UB', 'Upper Back'),
    ('LB', 'Lower Back'),
    ('LE', 'Legs'),
    ('CA', 'Calf'),
    ('BI', 'Biceps'),
    ('TR' ,'Triceps'),
    ('AB', 'Abs')
)
# Create your models here.

class ExerciseType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(choices = MUSCLE_GROUP)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.sets} x {self.reps}'

class Workout(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField('Workout Date')
    notes = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f'{self.name} on {self.date}'