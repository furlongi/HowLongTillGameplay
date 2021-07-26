from django.urls import path

from . import views

app_name = 'gamedata'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:name>', views.index, name='index')
]
