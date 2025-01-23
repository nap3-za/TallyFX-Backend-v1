from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name="tasks"


urlpatterns = [
]


routine_router = DefaultRouter()
routine_router.register("routine", views.RoutineViewSet, basename="routine")
urlpatterns += routine_router.urls

task_router = DefaultRouter()
task_router.register("task", views.TaskViewSet, basename="task")
urlpatterns += task_router.urls