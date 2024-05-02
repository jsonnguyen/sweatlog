from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('workouts/', views.WorkoutList.as_view(), name='index'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='detail'),
    path('workouts/create', views.WorkoutCreate.as_view(), name='workout_create'),
    path('workouts/<int:pk>/update', views.WorkoutUpdate.as_view(), name='workout_update'),
    path('workouts/<int:pk>/delete', views.WorkoutDelete.as_view(), name='workout_delete'),
    path('workouts/<int:workout_id>/add_exercise/', views.add_exercise, name='add_exercise'),
    path('workouts/<int:workout_id>/delete_exercise/<int:exercise_id>', views.delete_exercise, name='delete_exercise'),
    path('exercises/', views.ExerciseTypeList.as_view(), name='exercise_index'),
    path('exercises/<int:exercise_type_id>/', views.exercise_type_detail, name='exercise_detail'),
    path('exercises/create/', views.ExerciseTypeCreate.as_view(), name='exercise_create'),
    path('exercises/<int:pk>/update/', views.ExerciseTypeUpdate.as_view(), name='exercise_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseTypeDelete.as_view(), name='exercise_delete'),
]
