from django.urls import path, re_path

from . import views

app_name = 'gamedata'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('submit', views.submit, name='submit')
]
