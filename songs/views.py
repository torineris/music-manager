from pyexpat import model
from re import template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Music, Artist

from django.urls import reverse_lazy

# Create your views here.

#################### lists #######################


class ArtistList(ListView):
    model = Artist
    template_name = 'lists/artist.html'

class MusicList(ListView):
    model = Music
    template_name = 'lists/music.html'


#################### creations ###################


class ArtistCreate(CreateView):
    model = Artist
    fields = ['name']
    template_name = 'registers/form-artist.html'
    success_url = reverse_lazy('list-artist')


class MusicCreate(CreateView):
    model = Music
    fields = ['name','artist']
    template_name = 'registers/form-music.html'
    success_url = reverse_lazy('list-music')


#################### updates #######################


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name']
    template_name = 'registers/form-artist.html'
    success_url = reverse_lazy('list-artist')

class MusicUpdate(UpdateView):
    model = Music
    fields = ['name', 'artist']
    template_name = 'registers/form-music.html'
    success_url = reverse_lazy('list-music')


#################### updates #######################


class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'registers/form-delete.html'
    success_url = reverse_lazy('list-artist')

class MusicDelete(DeleteView):
    model = Music
    template_name = 'registers/form-delete.html'
    success_url = reverse_lazy('list-music')