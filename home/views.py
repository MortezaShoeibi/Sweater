from django.shortcuts import render
from .models import Sweat, About
from django.core.paginator import Paginator
from django.http.response import HttpResponse


def home(request) -> HttpResponse:
    objects_list = Sweat.objects.order_by("-created_at")
    paginator = Paginator(objects_list, 3)
    page_num = request.GET.get('page')
    sweats = paginator.get_page(page_num)
    return render(request, 'home/home.html', {'sweats': sweats})


def about(request) -> HttpResponse:
    about = About.objects.last()
    if about != None:
        pre_about = About.objects.filter(id=about.id - 1)
        pre_about.delete()
    return render(request, 'home/about.html', {'about': about})
