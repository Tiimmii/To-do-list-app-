from django.urls import path
from . import views

app_name="task"

urlpatterns = [
    path('Tasks', views.Tasklist.as_view(), name='task-list'),
    path('views/<str:pk>',views.TaskView.as_view(),name='task-view'),
    path('edit/<str:pk>',views.TaskEdit.as_view(),name='task-edit'),
    path('create',views.Taskcreate.as_view(),name='create'),
    path('delete/<str:pk>',views.Taskdelete.as_view(),name='task-delete'),
    
]