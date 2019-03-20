from django.urls import path, include
from . import views

app_name = 'artilheiros'
urlpatterns = [
    path('', views.index, name='artilheiros_index'),
]