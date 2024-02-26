from django.shortcuts import render
from works.models import portfolio,DescriptionWorks


def works(request):

    sliders = portfolio.objects.all()
    info = DescriptionWorks.objects.first()
    return render(request, "works/works.html", {'sliders':sliders, "info":info})