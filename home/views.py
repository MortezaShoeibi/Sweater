from django.shortcuts import render


def home(request) -> None:
    return render(request, 'home/home.html', {})
