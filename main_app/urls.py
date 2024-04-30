from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('workouts/', views.WorkoutList.as_view(), name='index'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='detail'),
    path('workouts/create', views.WorkoutCreate.as_view(), name='workout_create')
]
