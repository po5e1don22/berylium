from django.urls import path
from works.views import works

app_name = "works"

urlpatterns = [
    path ('', works, name = "works")
]
