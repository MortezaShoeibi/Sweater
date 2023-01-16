from django.shortcuts import render, get_object_or_404
from .models import Sweat, About
from django.core.paginator import Paginator
from django.http.response import HttpResponse, JsonResponse


def home(request) -> HttpResponse:
    request.session['likes'] = {}
    objects_list = Sweat.objects.order_by("-created_at")
    paginator = Paginator(objects_list, 3)
    page_num = request.GET.get('page')
    sweats = paginator.get_page(page_num)
    return render(request, 'home/home.html', {'sweats': sweats})


def sweat_details(request, pk) -> HttpResponse:
    sweat = get_object_or_404(Sweat, id=pk)
    return render(request, 'home/sweat.html', {'sweat': sweat})


def about(request) -> HttpResponse:
    about = About.objects.last()
    if about != None:
        pre_about = About.objects.filter(id=about.id - 1)
        pre_about.delete()
    return render(request, 'home/about.html', {'about': about})


def like(request, pk) -> JsonResponse:
    is_liked = request.session['likes'].get(f'sweat_number{pk}', False)
    sweat = Sweat.objects.get(id=pk)
    if is_liked:
        sweat.like -= 1
        sweat.save()
        request.session['likes'][f'sweat_number{pk}'] = False
        return JsonResponse({'response': 'unliked'})
    else:
        sweat.like += 1
        sweat.save()
        request.session['likes'][f'sweat_number{pk}'] = True
        return JsonResponse({'response': 'liked'})
