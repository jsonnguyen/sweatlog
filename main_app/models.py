from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExerciseType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_groups = models.ManyToManyField(MuscleGroup)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("exercise_detail", kwargs={"exercise_type_id": self.id})


class Workout(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField('Workout Date')
    notes = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} on {self.date}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"workout_id": self.id})
    
    class Meta:
        ordering = ['-date']
    
class Exercise(models.Model):
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.exercise_type.name} {self.sets} x {self.reps}'