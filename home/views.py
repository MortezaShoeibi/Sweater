from django.shortcuts import render
from .models import Sweat


def home(request) -> None:
    sweats = Sweat.objects.order_by("-created_at")
    return render(request, 'home/home.html', {'sweats': sweats})
