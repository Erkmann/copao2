from django.urls import path, include
from . import views

app_name = 'classificacao'
urlpatterns = [
    path('', views.index, name='classificacao_index'),
    ]