from django.shortcuts import render
from .models import Kurssi
from django.db.models.functions import Lower



# Create your views here.

def index(request):
    #etusivu ajanhallinnalle
    kurssit = Kurssi.objects.annotate(lower_kurssi=Lower('kurssi')).order_by('lower_kurssi') 
    #järjestää kurssit aakkosjärjestykseen huomioiden myös pienet alkukirjaimet
    return render(request, 'TimeManagementToolApp/index.html',{'kurssit': kurssit})

def kurssit(request):
    #kaikki kurssit
    kurssit = Kurssi.objects.annotate(lower_kurssi=Lower('kurssi')).order_by('lower_kurssi') 
    context = {'kurssit': kurssit}
    return render(request, 'TimeManagementToolApp/kurssit.html', context)

def kurssi(request, kurssi_id):
    #yhden kurssin lisätyt tehtävät
    kurssi = Kurssi.objects.get(id=kurssi_id)
    tehtavat = kurssi.teht_set.order_by('teht')
    context = {'kurssi': kurssi, 'teht': tehtavat}
    return render(request, 'TimeManagementToolApp/kurssi.html', context)

