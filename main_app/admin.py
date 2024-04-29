from django.contrib import admin
from .models import Workout, Exercise, ExerciseType, MuscleGroup

# Register your models here.
admin.site.register([
    Workout,
    Exercise,
    ExerciseType, 
    MuscleGroup
])