from django.contrib import admin
from .models import Workout, Exercise, ExerciseType

# Register your models here.
admin.site.register([
    Workout,
    Exercise,
    ExerciseType
])