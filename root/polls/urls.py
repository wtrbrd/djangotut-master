from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),   #why does this have to be blank to work?
    path('polls', views.index, name='index'),
    path('', views.books, name='books'),
]
# i cant get the pages to have sep. msgs 