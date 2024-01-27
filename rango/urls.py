from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.about, name='about'),
    path('', views.index, name='index'),
]