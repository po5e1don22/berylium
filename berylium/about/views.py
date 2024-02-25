from django.shortcuts import render
from about.models import TeamDescription,staff

def about(request):
    team_info =TeamDescription.objects.first()
    staff_info = staff.objects.all()
    return render(request, "about/about.html",{"team_info":team_info, "staff_info":staff_info })
