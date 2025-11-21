from django.urls import path
from . import views
urlpatterns = [
    path('', views.tasks_list, name="tasks_list"),
    path('create/', views.task_create, name="task_create"),
    path('update/<int:pk>/', views.task_update, name="task_update"),
    path('delete/<int:pk>/', views.task_delete, name="task_delete"),
]