from django.shortcuts import render
from .models import Kurssi

# Create your views here.

def index(request):
    #etusivu ajanhallinnalle
    kurssit = Kurssi.objects.all()
    return render(request, 'TimeManagementToolApp/index.html',{'kurssit': kurssit})
