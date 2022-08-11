from ast import Pass
from django.urls import path
from . import views

app_name="task"

urlpatterns = [
    path('', views.index, name='index'),
    path('views/<str:pk>',views.view,name='view'),
    path('search',views.search,name='search'),
    path('edit/<str:pk>',views.edit,name='edit'),
    path('create',views.create,name='create'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    
]