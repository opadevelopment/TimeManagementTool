from django.urls import path
from . import views

app_name = 'TimeManagementToolApp'
urlpatterns = [
    #etusivu
    path('', views.index, name='index'),
    #kurssit-sivu
    path('kurssit/', views.kurssit, name='kurssit'),
    #Valitun kurssin oma sivu
    path('kurssit/<int:kurssi_id>/', views.kurssi, name='kurssi'),
]