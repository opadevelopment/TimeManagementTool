from django.shortcuts import render, redirect,get_object_or_404
from .models import Kurssi, Teht
from django.db.models.functions import Lower
from .forms import KurssiForm, TehtForm
from django.urls import reverse



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


def lisaa_kurssi(request):
    #Lisää uusi kurssi
    if request.method != 'POST':
        #Luodaan tyhjä lomake
        form = KurssiForm()

    else:
        #Käsitellään data
        form = KurssiForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('TimeManagementToolApp:kurssit')

    #Näytetään tyhjä lomake
    context = {'form': form}
    return render(request, 'TimeManagementToolApp/lisaa_kurssi.html', context)

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

def muokkaa_tehtava(request, teht_id):
    #Muokataan olemassa olevaa tehtävää
    teht= Teht.objects.get(id=teht_id)
    kurssi = teht.kurssi
    # Lisätään kun userit käytössä
    # Suojataan muokkausoikeus vain oikealle käyttäjälle
    """if kurssi.owner != request.user:
        raise Http404""" 

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

def delete_teht(request, teht_id):
    teht = get_object_or_404(Teht, id=teht_id)
    if request.method == 'POST':
        teht.delete()
        return redirect(reverse('TimeManagementToolApp:kurssi'))  # Redirect to a relevant page
    return render(request, 'delete_confirm.html', {'teht': teht})