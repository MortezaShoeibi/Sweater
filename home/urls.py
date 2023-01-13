from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sweat/<int:pk>', views.sweat_details, name='sweat'),
    path('sweat/like/<int:pk>', views.like, name='like'),
]
