from django.urls import path
from . import views

app_name = 'TimeManagementToolApp'
urlpatterns = [
    #etusivu
    path('', views.index, name='index')
]