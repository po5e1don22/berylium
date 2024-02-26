from django.shortcuts import render
from service.models import ServicesDescription

def service(request):
    info = ServicesDescription.objects.first()
    return render (request, "service/services.html", {'info':info})

