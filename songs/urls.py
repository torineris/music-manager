from django.urls import path
from .views import ArtistDelete, ArtistList, ArtistUpdate, MusicDelete,MusicList, MusicUpdate
from .views import ArtistCreate, MusicCreate


urlpatterns = [
    path('list/artist', ArtistList.as_view(), name='list-artist'),
    path('list/music', MusicList.as_view(), name='list-music'),

    path('add/artist', ArtistCreate.as_view(), name='add-artist'),
    path('add/music', MusicCreate.as_view(), name='add-music'),

    path('edit/artist/<int:pk>', ArtistUpdate.as_view(), name='edit-artist'),
    path('edit/music/<int:pk>', MusicUpdate.as_view(), name='edit-music'),

    path('delete/artist/<int:pk>', ArtistDelete.as_view(), name='delete-artist'),
    path('delete/music/<int:pk>', MusicDelete.as_view(), name='delete-music'),
]