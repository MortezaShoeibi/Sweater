from django.shortcuts import render
from .models import Sweat
from django.core.paginator import Paginator


def home(request) -> None:
    objects_list = Sweat.objects.order_by("-created_at")
    paginator = Paginator(objects_list, 4)
    page_num = request.GET.get('page')
    sweats = paginator.get_page(page_num)
    return render(request, 'home/home.html', {'sweats': sweats})
