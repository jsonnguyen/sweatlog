from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout
from .forms import ExerciseForm
# Create your views here.

def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def workout_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  exercise_form = ExerciseForm()
  return render(request, 'workouts/detail.html', {
    'workout': workout,
    'exercise_form': exercise_form
  })

class WorkoutList(LoginRequiredMixin, ListView):
  model = Workout

class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  fields = ['name', 'date', 'notes']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class WorkoutUpdate(LoginRequiredMixin, UpdateView):
  model = Workout
  fields = ['name', 'date', 'notes']

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url ='/workouts'