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
     #Lisää kurssi -sivu
    path('kurssit/lisaa_kurssi', views.lisaa_kurssi, name='lisaa_kurssi'),
    #Muokkaa tehtävää sivu
    path('muokkaa_tehtava/<int:teht_id>', views.muokkaa_tehtava, name='muokkaa_tehtava'),
    #Lisää tehtävä -sivu
    path('lisaa_tehtava/<int:kurssi_id>/', views.lisaa_tehtava, name='lisaa_tehtava'),
]
