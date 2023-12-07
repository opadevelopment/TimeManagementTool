from django.shortcuts import render
from .models import Kurssi
from django.db.models.functions import Lower

# Create your views here.

def index(request):
    #etusivu ajanhallinnalle
   kurssit = Kurssi.objects.annotate(lower_kurssi=Lower('kurssi')).order_by('lower_kurssi')
   return render(request, 'TimeManagementToolApp/index.html',{'kurssit': kurssit})
