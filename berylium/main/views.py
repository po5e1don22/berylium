from django.shortcuts import render
from main.models import pic_slider, main

def index(request):
    slides = pic_slider.objects.all()
    pictures = main.objects.all()
    return render(request,"main/index.html",{"slides":slides,'pictures':pictures})