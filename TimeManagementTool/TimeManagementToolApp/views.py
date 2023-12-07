from django.shortcuts import render

# Create your views here.

def index(request):
    #etusivu ajanhallinnalle
    return render(request, 'TimeManagementToolApp/index.html')
