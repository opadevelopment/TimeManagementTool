#url patternit käyttäjille

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #rekisteröintisivu
    path('rekist/', views.rekist, name='rekist'),
]