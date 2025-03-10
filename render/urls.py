from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rm-bg', views.remove_background),
]
