from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Kurssi, Teht
from django.db.models.functions import Lower
from .forms import KurssiForm, TehtForm
from django.http import Http404

# Create your views here.

@login_required
def index(request):
    #etusivu ajanhallinnalle
    kurssit = Kurssi.objects.annotate(lower_kurssi=Lower('kurssi')).order_by('lower_kurssi') 
    #järjestää kurssit aakkosjärjestykseen huomioiden myös pienet alkukirjaimet
    return render(request, 'TimeManagementToolApp/index.html',{'kurssit': kurssit})

@login_required
def kurssit(request):
    #kaikki kurssit
    kurssit = Kurssi.objects.filter(kayttaja=request.user).order_by(Lower('kurssi')) 
    context = {'kurssit': kurssit}
    return render(request, 'TimeManagementToolApp/kurssit.html', context)

@login_required
def kurssi(request, kurssi_id):
    #yhden kurssin lisätyt tehtävät
    kurssi = Kurssi.objects.get(id=kurssi_id)
    #varmistetaan, että kurssi kuuluu käyttäjälle
    if kurssi.kayttaja != request.user:
        raise Http404
    tehtavat = kurssi.teht_set.order_by('teht')
    context = {'kurssi': kurssi, 'teht': tehtavat}
    return render(request, 'TimeManagementToolApp/kurssi.html', context)

@login_required
def lisaa_kurssi(request):
    #Lisää uusi kurssi
    if request.method != 'POST':
        #Luodaan tyhjä lomake
        form = KurssiForm()

    else:
        #Käsitellään data
        form = KurssiForm(data=request.POST)
        if form.is_valid():
            lisaa_kurssi = form.save(commit=False)
            lisaa_kurssi.kayttaja = request.user
            lisaa_kurssi.save()
            return redirect('TimeManagementToolApp:kurssit')

    #Näytetään tyhjä lomake
    context = {'form': form}
    return render(request, 'TimeManagementToolApp/lisaa_kurssi.html', context)

@login_required
def lisaa_tehtava(request, kurssi_id):
    #Lisää uusi tehtävä tietyn kurssin alle
    kurssi = Kurssi.objects.get(id=kurssi_id)

    if request.method != 'POST':
        #Luo tyhjä lomake
        form = TehtForm()

    else:
        #Käsitellään data
        form = TehtForm(data=request.POST or None)
        if form.is_valid():
            lisaa_tehtava = form.save(commit=False)
            lisaa_tehtava.kurssi = kurssi
            lisaa_tehtava.save()
            return redirect('TimeManagementToolApp:kurssi', kurssi_id=kurssi_id)

    #Näytetään tyhjä lomake
    context = {'kurssi': kurssi, 'form':form}
    return render(request, 'TimeManagementToolApp/lisaa_tehtava.html', context)

@login_required
def muokkaa_tehtava(request, teht_id):
    #Muokataan olemassa olevaa tehtävää
    teht= Teht.objects.get(id=teht_id)
    kurssi = teht.kurssi
    # Lisätään kun userit käytössä
    # Suojataan muokkausoikeus vain oikealle käyttäjälle
    if kurssi.kayttaja != request.user:
        raise Http404

    if request.method != 'POST':
        #Esitäytetty alkuperäisen tehtävän sisällön mukaan
        form = TehtForm(instance=teht)

    else:
        #Käsitellään muutokset
        form = TehtForm(instance=teht, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('TimeManagementToolApp:kurssi', kurssi_id =kurssi.id)
        
    context = {'teht': teht, 'kurssi': kurssi, 'form': form}
    return render(request, 'TimeManagementToolApp/muokkaa_tehtava.html', context)

