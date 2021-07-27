from django.urls import path

from . import views

app_name = 'gamedata'
urlpatterns = [
    path('search', views.index, name='index'),
    path('submit', views.submit, name='submit')
]
