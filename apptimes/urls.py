from django.urls import path, include
from . import views

app_name = 'time'
urlpatterns = [
    path('', views.index, name='times_index'),
    path('time/<int:pk>', views.time, name='time_view'),
]